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


def _print_issue(issue_model):
    json_obj = json.loads(issue_model.raw_data)
    title = json_obj["title"]
    num = json_obj["number"]
    num_comments = issue_model.comments.count()
    print(f"#{num} {title} ({num_comments} comments)")
    related_issues = []
    duplicate_of = []

    def process_body(body):
        # print(f'{body}')
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

    print(f"\tRelated to {list(set(related_issues))}")
    print(f"\tDuplicate of {list(set(duplicate_of))}")


def print_all(instance):
    db = instance.get_db()
    for issue in db.session.query(Issue).order_by(Issue.number).all():
        _print_issue(issue)


def print_single(instance, number):
    db = instance.get_db()
    issue_model = db.session.query(Issue).filter(Issue.number == number).first()
    if issue_model is None:
        print(f"Issue #{number} is not in the DB")
    else:
        _print_issue(issue_model)


def main(argv):

    instance = Instance()
    if len(argv) > 1:
        print_single(instance, int(argv[1]))
    else:
        print_all(instance)


if __name__ == "__main__":
    main(sys.argv)
