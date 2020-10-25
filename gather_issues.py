import sys
import json
import re
import github
from github import Github
from common.Instance import get_github_token, get_github_repo, Instance
from models.Issue import Issue
from models.Comment import Comment

"""
This is a test script for caching an issue into our database.

Since we've got an enormous number of issues and comments to parse, we can't
just query their DB at runtime. We'll need to cache the results locally.
"""


def many_usage():
    print("python gather_issues.py many [start] [end]")
    print("    This will fetch all issues in the given range")


def single_usage():
    print("python gather_issues.py single [issue_number]")
    print(
        "    This will fetch the given issue from the database, or fetch it from github and cache it in our database."
    )


def usage():
    print("python gather_issues.py (single|many) [args...]")
    print(
        "    single can be used for fetching a single isse from the DB or API"
        "    mane can be used for fetching a range of issues from the API and caching them"
    )


def cache_many_issues(instance, start_number, end_number):
    db = instance.get_db()
    if start_number >= end_number:
        return

    print(
        f"fetching issues {start_number} to {end_number} ({end_number-start_number} total)"
    )
    g = None  # Github(get_github_token())
    repo = None  # g.get_repo(get_github_repo())
    for i in range(start_number, end_number):
        issue_model = db.session.query(Issue).filter(Issue.number == i).first()
        if issue_model is None:
            if repo is None:
                # log into GH using token
                g = Github(get_github_token())
                repo = g.get_repo(get_github_repo())

            try:
                issue = repo.get_issue(number=i)
                issue_model = Issue(issue)
                db.session.add(issue_model)
                db.session.commit()
                print(f"cached #{issue_model.number}")
            except Exception as e:
                print(e)
        else:
            print(f"already had #{issue_model.number} in the DB")


def lookup_single_issue(instance, issue_number):

    db = instance.get_db()

    issue_model = db.session.query(Issue).filter(Issue.number == issue_number).first()
    if issue_model is None:
        print(f"Did not find existing issue {issue_number}")

        # log into GH using token
        g = Github(get_github_token())
        repo = g.get_repo(get_github_repo())
        try:
            issue = repo.get_issue(number=issue_number)

            issue_model = Issue(issue)
            db.session.add(issue_model)
            # db.session.commit()
            print("created new DB object for issue")

            comments = issue.get_comments()
            print(f"Issue has {comments.totalCount} comments")
            for comment in comments:
                api_id = comment.id
                print(f"looking for comment {api_id}...")
                comment_model = (
                    db.session.query(Comment).filter(Comment.api_id == api_id).first()
                )
                if comment_model is None:
                    comment_model = Comment(issue, comment)
                    db.session.add(comment_model)
                    print(f"\tcreated comment object")
                else:
                    print(f"\tAready had this comment")
            db.session.commit()
        except Exception as e:
            print(e)

    print(f"Found issue #{issue_number} in object with ID={issue_model.id}")
    # print(f'number={issue_model.number}')
    # print(f"\n{issue_model.raw_data}")
    json_obj = json.loads(issue_model.raw_data)
    title = json_obj["title"]
    num = json_obj["number"]
    num_comments = issue_model.comments.count()
    print(f"#{num} {title} ({num_comments} comments)")


def main(argv):

    if len(argv) < 2:
        usage()
        return

    instance = Instance()

    command = argv[1]
    if command == "single":
        if len(argv) < 3:
            single_usage()
            return
        lookup_single_issue(instance, int(argv[2]))
    elif command == "many":
        if len(argv) < 4:
            many_usage()
            return
        cache_many_issues(instance, int(argv[2]), int(argv[3]))


if __name__ == "__main__":
    main(sys.argv)
