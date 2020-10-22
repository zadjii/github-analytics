import github
import sys
import json

from github import Github
from common.Instance import get_github_token, get_github_repo


def do_on_all(transactions, callback):
    # type: ([Transaction], (Transaction, int)->Any) -> Any
    for index, transaction in enumerate(transactions):
        callback(transaction, index)


def export_as_json(issues):
    print('{ "issues": [')

    def do(t, i):
        if i > 0:
            print("\t,{}".format(t.serialize()))
        else:
            print("\t{}".format(t.serialize()))

    do_on_all(issues, do)
    print("]}")


class MyIssue(object):
    def __init__(self, api_object):
        # self.raw_data = api_object._rawData
        self.title = api_object.title
        self.number = api_object.number
        self.comments = []

    def serialize(self):
        return json.dumps(self.__dict__)


class MyComment(object):
    def __init__(self, api_object):
        self.raw_data = api_object._rawData
        self.id = api_object.id
        self.body = api_object.body

    def serialize(self):
        return json.dumps(self.__dict__)


def main(argv):
    gathered_issues = []

    # First create a Github instance:

    # using username and password
    g = Github(get_github_token())
    repo = g.get_repo(get_github_repo())
    # all_issues = repo.get_issues(state='all')
    # open_issues = repo.get_issues(state='open')
    # closed_issues = repo.get_issues(state='closed')
    label = repo.get_label("Resolution-Duplicate")
    duplicate_issues = repo.get_issues(labels=[label], state="all")

    issues = duplicate_issues

    for issue in issues:
        title = issue.title
        number = issue.number

        my_issue = MyIssue(issue)

        comments = issue.get_comments()
        for comment in comments:
            id = comment.id
            body = comment.body
            my_issue.comments.append({"id": id, "body": body})
        #     my_comment = MyComment(comment)
        #     my_issue.comments.append(my_comment)

        gathered_issues.append(my_issue)

    export_as_json(gathered_issues)


# {
#     "number": 1234,
#     "title": "",
#     "comments": [
#         {
#             "body": 4567,
#             "id": ""
#         }
#     ]
# }
if __name__ == "__main__":
    main(sys.argv)
