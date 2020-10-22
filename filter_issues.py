import sys
import json

def usage():
    pass

def main(argv):

    if len(argv) < 2:
        usage()
        return

    input_filename = argv[1]
    print('Loading issues from {}'.format(input_filename))
    gathered_issues = []
    with open(input_filename, 'rb') as jsonfile:
        all_issues_dict = json.load(jsonfile)
        for issue in all_issues_dict['issues']:
            gathered_issues.append( {'number': issue['number'], 'title': issue['title']} )

    print(json.dumps(gathered_issues))


if __name__ == '__main__':
    main(sys.argv)
