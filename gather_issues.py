import sys
import json
import re
import github
from github import Github
from common.Instance import get_github_token, get_github_repo, Instance
from models.Issue import Issue

"""
This is a test script for caching an issue into our database.

Since we've got an enormous number of issues and comments to parse, we can't
just query their DB at runtime. We'll need to cache the results locally.
"""


def usage():
    print("python gather_issues.py [issue_number]")
    print(
        "    This will fetch the given issue from the database, or fetch it from github and cache it in our database."
    )
    pass


def main(argv):

    if len(argv) < 2:
        usage()
        return

    number_from_cmdline = int(argv[1])

    instance = Instance()
    db = instance.get_db()

    issue_model = (
        db.session.query(Issue).filter(Issue.number == number_from_cmdline).first()
    )
    if issue_model is None:
        print(f"Did not find existing issue {number_from_cmdline}")

        # log into GH using token
        g = Github(get_github_token())
        repo = g.get_repo(get_github_repo())
        issue = repo.get_issue(number=number_from_cmdline)

        issue_model = Issue(issue)
        db.session.add(issue_model)
        db.session.commit()
        print("created new DB object")

    print(f"Found issue #{number_from_cmdline} in object with ID={issue_model.id}")
    # print(f'number={issue_model.number}')
    print(f"\n{issue_model.raw_data}")


if __name__ == "__main__":
    main(sys.argv)
