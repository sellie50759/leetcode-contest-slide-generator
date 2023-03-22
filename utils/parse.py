import requests
import json
from bs4 import BeautifulSoup


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
        if is_biweekly:
            leetcode_constest_url = f"https://leetcode.com/contest/api/info/biweekly-contest-{contest_id}/"
        else:
            leetcode_constest_url = f"https://leetcode.com/contest/api/info/weekly-contest-{contest_id}/"

        contest_page = requests.get(leetcode_constest_url)
        contest_data = contest_page.json()

        print(contest_data['questions'])
        contest_data['questions']

    def getContest(self):
        if len(self._problems) == 0:
            self.crawlContestInformation()


if __name__ == "__main__":
    # 教學 https://blog.csdn.net/weixin_45394002/article/details/121125753
    contest = LeetcodeContest(100, is_biweekly=True)
