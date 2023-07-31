from utils.leetcode_contest import LeetcodeContest
from utils.hackmdapi import uploadNote, getTeamNotes
import argparse


def ext_check(expected_extension, openner):
    def extension(filename):
        if not filename.lower().endswith(expected_extension):
            raise ValueError()
        return openner(filename)
    return extension


def checkNoteExist(contest_id, is_biweekly):
    if is_biweekly:
        note_title = f"BiWeekly Contest {contest_id}"
    else:
        note_title = f"Weekly Contest {contest_id}"

    team_notes = getTeamNotes()

    for note in team_notes:
        if note_title == note['title']:
            return True
    return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='leetcode-contest-slide-generator',
        description='Generate Leetcode Contest Slide',
    )
    parser.add_argument('contest_id', type=int,
                        help='Leetcode contest id, input -1 represent get latest contest')
    parser.add_argument('--is_biweekly',
                        action=argparse.BooleanOptionalAction,
                        help='this contest is biweekly or weekly contest'
                        )

    parser.add_argument('-o', '--output',
                        required=False,
                        type=ext_check('.md', argparse.FileType('w')),
                        help='Slide output_path')

    args = parser.parse_args()

    contest_id = args.contest_id
    is_biweekly = args.is_biweekly

    if contest_id == -1:
        contest_id = LeetcodeContest.getLatestContestId(is_biweekly)

    if not args.output:
        output_path = f'./{contest_id}_slide.md'
    else:
        output_path = args.output

    # prevent reupload same note
    if checkNoteExist(contest_id, is_biweekly):
        print("Note already exist")
        exit(0)

    # try:
    contest = LeetcodeContest(contest_id, is_biweekly)

    contest.to_md(output_path)

    uploadNote(output_path)
    # except Exception as e:
        # print(str(e))
        # exit(1)

    '''
    contest_id, is_biweekly = -1, True

    if contest_id == -1:
        latest_contest_id = LeetcodeContest.getLatestContestId(is_biweekly)

        if checkNoteExist(latest_contest_id, is_biweekly):
            print("Note already exist")
            exit(0)
    '''
