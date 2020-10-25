import sys
import json
import re
import github
from github import Github
from common.Instance import get_github_token, get_github_repo, Instance
from models.Issue import Issue
from models.Comment import Comment


def usage():
    print("python list_dupes.py ")
    print("    <todo>")


def _print_issue(db, issue_model):
    json_obj = json.loads(issue_model.raw_data)
    title = json_obj["title"]
    num = json_obj["number"]
    num_comments = issue_model.comments.count()
    print(f"#{num} {title} ({num_comments} comments)")
    related_issues = []
    duplicate_of = []

    def process_body(body):
        # print(f'{body}')
        if body is None or body == "":
            return
        strong_dupes = re.findall(r"/dup((licate)|(e))?( of)? #(\d+)\s*", body)
        for match in strong_dupes:
            dupe_number = int(match[-1])
            duplicate_of.append(dupe_number)

        mentioned_issues = re.findall(r"#(\d+)\s*", body)
        # print(f"{mentioned_issues}")
        for match in mentioned_issues:
            mentioned_num = int(match)
            related_issues.append(mentioned_num)

    process_body(json_obj["body"])

    for comment in issue_model.comments:
        comment_json = json.loads(comment.raw_data)
        body = comment_json["body"]
        process_body(body)

    related_issues = list(set(related_issues))
    duplicate_of = list(set(duplicate_of))

    db.session.add(issue_model)
    for issue_num in related_issues:
        other = db.session.query(Issue).filter(Issue.number == issue_num).first()
        if other is not None:
            issue_model.mentioned_issues.append(other)
            db.session.add(other)

    for issue_num in duplicate_of:
        other = db.session.query(Issue).filter(Issue.number == issue_num).first()
        if other is not None:
            issue_model.duplicate_of.append(other)
            db.session.add(other)

    print(f"\tRelated to {list(set(related_issues))}")
    print(f"\tDuplicate of {list(set(duplicate_of))}")

    duplicates = [other.number for other in issue_model.duplicates]
    mentioned_by = [other.number for other in issue_model.mentioned_by]
    print(f"\tduplicates: {duplicates}")
    print(f"\tmentioned_by: {mentioned_by}")

    duplicate_of_results = [other.number for other in issue_model.duplicate_of]
    mentioned_issues_results = [other.number for other in issue_model.mentioned_issues]
    print(f"\tduplicate_of_results: {duplicate_of_results}")
    print(f"\tmentioned_issues_results: {mentioned_issues_results}")

    db.session.commit()


def print_range(instance, min_num, max_num):
    db = instance.get_db()

    for issue in db.session.query(Issue).order_by(Issue.number).all():
        if issue.number < min_num or issue.number > max_num:
            continue
        _print_issue(db, issue)


def print_all(instance):
    db = instance.get_db()

    for issue in db.session.query(Issue).order_by(Issue.number).all():
        # [issue.mentioned_by.remove(other) for other in issue.mentioned_by]
        # [issue.mentioned_issues.remove(other) for other in issue.mentioned_issues]
        # [issue.duplicates.remove(other) for other in issue.duplicates]
        # [issue.duplicate_of.remove(other) for other in issue.duplicate_of]

        # issue.mentioned_by = []
        # issue.mentioned_issues = []
        # issue.duplicates = []
        # issue.duplicate_of = []

        db.session.add(issue)
        db.session.commit()
        print(f"cleared issue #{issue.number}")

    for issue in db.session.query(Issue).order_by(Issue.number).all():
        _print_issue(db, issue)


def print_single(instance, number):
    db = instance.get_db()
    issue_model = db.session.query(Issue).filter(Issue.number == number).first()
    if issue_model is None:
        print(f"Issue #{number} is not in the DB")
    else:
        _print_issue(db, issue_model)


def main(argv):

    instance = Instance()
    if len(argv) > 2:
        print_range(instance, int(argv[1]), int(argv[2]))
    elif len(argv) > 1:
        print_single(instance, int(argv[1]))
    else:
        print_all(instance)


if __name__ == "__main__":
    main(sys.argv)
