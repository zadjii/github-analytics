import sys
import json
import re
import datetime
import github
from github import Github
from common.Instance import get_github_token, get_github_repo, Instance

"""
TODO!
"""


def usage():
    print("python bug-jail.py ")
    print("    TODO")


class IssueGroup(object):
    def __init__(self, title):
        self.title = title
        self.issues = []


def do_the_thing(instance, markdown=False):

    # log into GH using token
    g = Github(get_github_token())
    repo = g.get_repo(get_github_repo())
    try:
        milestone_1_14 = repo.get_milestone(number=41)
        milestone_22h1 = repo.get_milestone(number=43)
        milestone_22h2 = repo.get_milestone(number=44)

        labels = {
            "task": repo.get_label("Issue-Task"),
            "feature": repo.get_label("Issue-Feature"),
            "bug": repo.get_label("Issue-Bug"),
            "p0": repo.get_label("Priority-0"),
            "p1": repo.get_label("Priority-1"),
            "p2": repo.get_label("Priority-2"),
            "p3": repo.get_label("Priority-3"),
            "a11y": repo.get_label("Area-Accessibility"),
            "perf": repo.get_label("Area-Performance"),
            "rendering": repo.get_label("Area-Rendering"),
            "loc": repo.get_label("Area-Localization"),
            "atlas": repo.get_label("Area-AtlasEngine"),
            "defterm": repo.get_label("Area-DefApp"),
            "i18n": repo.get_label("Area-i18n"),
            "termcontrol": repo.get_label("Area-TerminalControl"),
            "input": repo.get_label("Area-Input"),
            "sui": repo.get_label("Area-Settings UI"),
            "conhost": repo.get_label("Product-Conhost"),
            "conpty": repo.get_label("Product-Conpty"),
            "fixed": repo.get_label("Resolution-Fix-Committed"),
            "in-pr": repo.get_label("In-PR"),
        }

        issues_1_14 = repo.get_issues(milestone=milestone_1_14, state="open")
        print(f"{issues_1_14.totalCount} open issues\n")

        # issues_22h1 = repo.get_issues(milestone=milestone_22h1, state="open", labels=[labels["bug"]])
        # open_issues = issues_22h1.totalCount

        groups = []

        ime = IssueGroup("IME support")
        groups.append(ime)
        loc = IssueGroup("Localization")
        groups.append(loc)
        defterm = IssueGroup("DefApp")
        groups.append(defterm)
        perf = IssueGroup("Performance / Rendering")
        groups.append(perf)
        alt = IssueGroup("Alt Buffer")
        groups.append(alt)
        a11y = IssueGroup("A11y")
        groups.append(a11y)
        conhost = IssueGroup("Misc Conhost bugs")
        groups.append(conhost)
        conpty = IssueGroup("Misc Conpty")
        groups.append(conpty)
        sui = IssueGroup("SUI / Settings")
        groups.append(sui)
        other = IssueGroup("Others")
        groups.append(other)

        if not markdown:
            sys.stdout.write(f"Sorting")

        for issue in issues_1_14:
            found_home = False
            if not markdown:
                sys.stdout.write(f".")

            if labels["defterm"] in issue.labels:
                defterm.issues.append(issue)
                continue
            if labels["a11y"] in issue.labels:
                a11y.issues.append(issue)
                continue
            if labels["loc"] in issue.labels:
                loc.issues.append(issue)
                continue
            if labels["perf"] in issue.labels:
                perf.issues.append(issue)
                continue

            if (labels["input"] in issue.labels and labels["i18n"] in issue.labels and labels["termcontrol"] in issue.labels) or "IME" in issue.title:
                ime.issues.append(issue)
                continue

            if labels["rendering"] in issue.labels:
                perf.issues.append(issue)
                continue
            if labels["sui"] in issue.labels:
                sui.issues.append(issue)
                continue


            if "alt buffer" in issue.title or "Alternate screen" in issue.title or "alternate screen" in issue.title:
                alt.issues.append(issue)
                continue

            if labels["conpty"] in issue.labels:
                conpty.issues.append(issue)
                continue
            if labels["conhost"] in issue.labels:
                conhost.issues.append(issue)
                continue

            if not found_home:
                other.issues.append(issue)

        sys.stdout.write(f"\n")

        # for issue in issues_22h1:
        #     print(f"* [ ] #{issue.number} {issue.title}")

        for g in groups:
            print(f"### {g.title} {len(g.issues)}")
            for issue in g.issues:
                fixed = labels["in-pr"] in issue.labels or labels["fixed"] in issue.labels
                fix = 'x' if fixed else ' '
                issue_num = f"[#{issue.number}]" if markdown else f"\x1b]8;;https://github.com/microsoft/terminal/issues/{issue.number}\x1b\\#{issue.number}\x1b]8;;\x1b\\"
                print(f"* [{fix}] {issue_num} {issue.title}")
            if markdown:
                print("\n")

        if markdown:
            for g in groups:
                for i in g.issues:
                    print(f"[#{issue.number}]: https://github.com/microsoft/terminal/issues/{issue.number}")

    except Exception as e:
        print(e)


def main(argv):

    # if len(argv) < 2:
    #     usage()
    #     return

    instance = Instance()

    if len(argv) == 2:
        command = argv[1]
        if command == "--help" or command == "-h" or command == "-?" or command == "/?":
            usage()
            return
        elif command == "md":
            do_the_thing(instance, markdown=True)
            return
    else:
        do_the_thing(instance)


if __name__ == "__main__":
    main(sys.argv)
