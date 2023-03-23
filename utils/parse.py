from leetcodeapi import *

class Problem:
    def __init__(self, title, url, difficulty, constraint):
        self._title = title  # 題目標題
        self._url = url  # 題目連結
        self._difficulty = difficulty  # 題目難度
        self._constraint = constraint  # 題目限制

    def __getattr__(self, name: str):
        return self.__dict__[f"_{name}"]


class LeetcodeContest:
    def __init__(self, contest_id, is_biweekly=False, latest=True):
        self._problems = []
        self.crawlContestInformation(contest_id, is_biweekly)

    def crawlContestInformation(self, contest_id, is_biweekly=False):
        problem_ids = get_contest_problem_ids(contest_id, is_biweekly)

        self._problems = get_problems(problem_ids)

    def getProblems(self):
        return self._problems


if __name__ == "__main__":
    contest = LeetcodeContest(100, is_biweekly=True)

    for problem in contest.getProblems():
        print(problem.title)
        print(problem.url)
        print(problem.difficulty)
        print(problem.constraint)