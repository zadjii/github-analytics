import sys
import json
import re
import github
from github import Github
from common.Instance import get_github_token, get_github_repo


def usage():
    pass


def main(argv):

    if len(argv) < 2:
        usage()
        return

    input_filename = argv[1]

    all_issues = []

    result = {"issues": [], "links": []}

    with open(input_filename, "rb") as jsonfile:
        all_issues_dict = json.load(jsonfile)
        # for issue in all_issues_dict['issues']:
        #     gathered_issues.append( {'number': issue['number'], 'title': issue['title']} )
        issues = all_issues_dict["issues"]

        graph_blobs = []
        for issue in issues:
            # issue = issues[0]
            issue_number = issue["number"]
            all_matches = []
            comments = issue["comments"]
            # all_issues.append(issue_number)
            for comment in comments:
                # comment = comments[0]
                body = comment["body"]
                matches = re.findall(r"/dup((licate)|(e))?( of)? #(\d+)\s*", body)
                # print(matches)
                for match in matches:
                    dupe_number = int(match[-1])
                    all_matches.append(dupe_number)
                    all_issues.append(dupe_number)
                # return
                # all_matches.extend(matches)
            if len(all_matches) > 0:
                # Only add an issue to the graph if it was actually marked as a dupe of another
                all_issues.append(issue_number)

                for m in all_matches:
                    result["links"].append({"source": issue_number, "target": m})
                    # graph_blobs.append(u'{{ "source": {}, "target": {} }}'.format(issue_number, m))
                # print('{}: {}'.format(issue_number, all_matches))

    issue_blobs = []
    set_of_issues = set(all_issues)

    # log into GH using token
    g = Github(get_github_token())
    repo = g.get_repo(get_github_repo())

    for i in set_of_issues:
        issue = repo.get_issue(number=i)
        title = issue.title
        state = issue.state
        # title = "test"
        # state = "open"
        # issue_blobs.append(u'{{ "number": {}, "title":\"{}\", "state":\"{}\" }}'.format(i, title, state))
        result["issues"].append(issue._rawData)
        # break

    # print('{\n')
    # issues_string = ',\n'.join(issue_blobs)
    # print(u'"issues":[{}],'.format(issues_string))

    # links_string = ',\n'.join(graph_blobs)
    # print(u'"links":[{}]'.format(links_string))
    # # print(links_string)
    # print('}\n')
    print(json.dumps(result))

    # print(json.dumps(gathered_issues))


if __name__ == "__main__":
    main(sys.argv)
