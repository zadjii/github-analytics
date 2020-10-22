import sys
import json
import re
import github
from github import Github
from common.Instance import get_github_token, get_github_repo, Instance
from models.Issue import Issue


def usage():
    print("python dump_issues.py ")
    print("    Print out the title of a single or all issues")


def _print_issue(issue_model):
    json_obj = json.loads(issue_model.raw_data)
    title = json_obj["title"]
    num = json_obj["number"]
    print(f"#{num} {title}")


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
