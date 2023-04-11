from utils.leetcode_api import *


class Problem:
    def __init__(self, title, url, difficulty, constraint, question_id):
        self._title = title  # 題目標題
        self._url = url  # 題目連結
        self._difficulty = difficulty  # 題目難度
        self._constraint = constraint  # 題目限制
        self._question_id = question_id

    def __getattr__(self, name: str):
        return self.__dict__[f"_{name}"]


def constructProblemStatement(problem):
    problem_statement = f'''
## [{problem.question_id}. {problem.title}]({problem.url})(<font color={LeetcodeContest.difficulty_map[problem.difficulty][0]}>{LeetcodeContest.difficulty_map[problem.difficulty][1]}</font>)\n
限制 :\n
{problem.constraint}\n
### Solution\n
#### 時間複雜度: ***O()***\n
#### 空間複雜度: ***O()***\n
程式碼:\n
```c++=\n
```\n
'''
    return problem_statement


class LeetcodeContest:
    difficulty_map = {
                    1: ('#00B8A3', 'Easy'),
                    2: ('#FFC011', 'Medium'),
                    3: ('#FF375F', 'Hard'),
                    }

    def __init__(self, contest_id, is_biweekly=False, latest=True):
        self._problems = []
        self._is_biweekly = is_biweekly
        self._contest_id = contest_id
        self.crawlContestInformation(contest_id, is_biweekly)

    def crawlContestInformation(self, contest_id, is_biweekly=False):
        problem_ids = get_contest_problem_ids(contest_id, is_biweekly)

        self._problems = [Problem(problem[0], problem[1], problem[2], problem[3], problem[4]) for problem in get_problems(problem_ids)]

    def getProblems(self):
        return self._problems

    def to_md(self, output_file):
        with open(output_file, 'w') as f:
            if self._is_biweekly:
                f.write(f'###### tags: `BiWeekly Contest`\n\
                # BiWeekly Contest {self._contest_id}\n')
            else:
                f.write(f'###### tags: `Weekly Contest`\n\
                # Weekly Contest {self._contest_id}\n')

            for problem in self._problems:
                problem_statement = constructProblemStatement(problem)
                f.write(problem_statement)


if __name__ == "__main__":
    contest_id = 337
    contest = LeetcodeContest(337)

    for problem in contest.getProblems():
        print(problem.title)
        print(problem.url)
        print(problem.difficulty)
        print(problem.constraint)
        print(problem.question_id)
