import sys
import json
import re
import github
from github import Github
from common.Instance import get_github_token, get_github_repo, Instance

"""
TODO!
"""


def usage():
    print("python collect_milestones.py ")
    print("    TODO")


def do_the_thing(instance):

    # log into GH using token
    g = Github(get_github_token())
    repo = g.get_repo(get_github_repo())
    try:
        milestone_22h1 = repo.get_milestone(number=43)
        milestone_22h2 = repo.get_milestone(number=44)

        labels = {
            "task": repo.get_label("Issue-Task"),
            "feature": repo.get_label("Issue-Feature"),
            "p0": repo.get_label("Priority-0"),
            "p1": repo.get_label("Priority-1"),
            "p2": repo.get_label("Priority-2"),
            "p3": repo.get_label("Priority-3"),
        }

        issues_22h1 = repo.get_issues(milestone=milestone_22h1, state="open")
        issues_22h2 = repo.get_issues(milestone=milestone_22h2, state="open")

        issues_2022 = issues_22h1.totalCount + issues_22h2.totalCount

        open_issues = repo.get_issues().totalCount
        open_prs = repo.get_pulls().totalCount

        total_p0s = (
            repo.get_issues(
                milestone=milestone_22h1, state="open", labels=[labels["p0"]]
            ).totalCount
            + repo.get_issues(
                milestone=milestone_22h2, state="open", labels=[labels["p0"]]
            ).totalCount
        )
        total_p1s = (
            repo.get_issues(
                milestone=milestone_22h1, state="open", labels=[labels["p1"]]
            ).totalCount
            + repo.get_issues(
                milestone=milestone_22h2, state="open", labels=[labels["p1"]]
            ).totalCount
        )
        total_p2s = (
            repo.get_issues(
                milestone=milestone_22h1, state="open", labels=[labels["p2"]]
            ).totalCount
            + repo.get_issues(
                milestone=milestone_22h2, state="open", labels=[labels["p2"]]
            ).totalCount
        )
        total_p3s = (
            repo.get_issues(
                milestone=milestone_22h1, state="open", labels=[labels["p3"]]
            ).totalCount
            + repo.get_issues(
                milestone=milestone_22h2, state="open", labels=[labels["p3"]]
            ).totalCount
        )
        total_tasks = (
            repo.get_issues(
                milestone=milestone_22h1, state="open", labels=[labels["task"]]
            ).totalCount
            + repo.get_issues(
                milestone=milestone_22h2, state="open", labels=[labels["task"]]
            ).totalCount
        )
        total_features = (
            repo.get_issues(
                milestone=milestone_22h1, state="open", labels=[labels["feature"]]
            ).totalCount
            + repo.get_issues(
                milestone=milestone_22h2, state="open", labels=[labels["feature"]]
            ).totalCount
        )

        print(f"{issues_22h1.totalCount} issues in 22H1")
        print(f"{issues_22h2.totalCount} issues in 22H2")

        print(f"{open_issues-open_prs}\tissues")
        print(f"{issues_2022}\t2022 issues")
        print(f"{total_p0s}\tp0s")
        print(f"{total_p1s}\tp1s")
        print(f"{total_p2s}\tp2s")
        print(f"{total_p3s}\tp3s")
        print(f"{total_tasks}\ttasks")
        print(f"{total_features}\tfeatures")
        print(f"{open_prs}\tPRs")

        print(
            f"{open_issues-open_prs},{issues_2022},{total_p0s},{total_p1s},{total_p2s},{total_p3s},{total_tasks}{total_features},{open_prs}"
        )

    except Exception as e:
        print(e)


def main(argv):

    # if len(argv) < 2:
    #     usage()
    #     return

    instance = Instance()

    # command = argv[1]

    do_the_thing(instance)


if __name__ == "__main__":
    main(sys.argv)
