from utils.leetcode_contest import LeetcodeContest
import argparse


def ext_check(expected_extension, openner):
    def extension(filename):
        if not filename.lower().endswith(expected_extension):
            raise ValueError()
        return openner(filename)
    return extension


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='leetcode-contest-slide-generator',
        description='Generate Leetcode Contest Slide',
    )
    parser.add_argument('contest_id', type=int,
                        help='Leetcode contest id')
    parser.add_argument('-i', '--is_biweekly',
                        required=False,
                        help='this contest is biweekly or weekly contest')
    parser.add_argument('-o', '--output',
                        required=False,
                        type=ext_check('.md', argparse.FileType('w')),
                        help='Slide output_path')

    args = parser.parse_args()
    contest_id = args.contest_id
    is_biweekly = bool(args.is_biweekly)

    if not args.output:
        output_path = f'./{contest_id}_slide.md'
    else:
        output_path = args.output

    contest = LeetcodeContest(contest_id, is_biweekly)

    contest.to_md(output_path)

