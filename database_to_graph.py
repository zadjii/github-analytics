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


def do_range(instance, min_num=None, max_num=None):
    db = instance.get_db()

    result = {"issues": [], "duplicate_of": [], "mentioned_issues": []}

    for issue in db.session.query(Issue).order_by(Issue.number).all():
        if min_num is not None and issue.number < min_num:
            continue
        if max_num is not None and issue.number > max_num:
            continue


        duplicates = [other.number for other in issue.duplicates]
        mentioned_by = [other.number for other in issue.mentioned_by]
        # print(f"\tduplicates: {duplicates}")
        # print(f"\tmentioned_by: {mentioned_by}")

        duplicate_of = [other.number for other in issue.duplicate_of]
        mentioned_issues = [other.number for other in issue.mentioned_issues]
        # print(f"\tduplicate_of_results: {duplicate_of_results}")
        # print(f"\tmentioned_issues_results: {mentioned_issues_results}")
        issue_dict = {
            "number": issue.number,
            "title": issue.title,
            "body": issue.body,
            "state": issue.state,

            "duplicates": duplicates,
            "mentioned_by": mentioned_by,
            "duplicate_of": duplicate_of,
            "mentioned_issues": mentioned_issues,
        }
        result['issues'].append(issue_dict)
        [result['duplicate_of'].append({'source': issue.number, 'target': other.number}) for other in issue.duplicate_of]
        [result['mentioned_issues'].append({'source': issue.number, 'target': other.number}) for other in issue.mentioned_issues]
        # print(f"Processed #{issue_model.number}")
        # print(json.dumps(issue_dict), indent=2)

    print(json.dumps(result, indent=2))

def main(argv):

    instance = Instance()
    if len(argv) > 2:
        do_range(instance, int(argv[1]), int(argv[2]))
    elif len(argv) > 1:
        do_range(instance, int(argv[1]))
    else:
        do_range(instance)


if __name__ == "__main__":
    main(sys.argv)
