import requests
import json
from bs4 import BeautifulSoup

session = requests.Session()
user_agent = r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'


def get_contest_problem_ids(contest_id, is_biweekly=False):
    if is_biweekly:
        leetcode_constest_url = f"https://leetcode.com/contest/api/info/biweekly-contest-{contest_id}/"
    else:
        leetcode_constest_url = f"https://leetcode.com/contest/api/info/weekly-contest-{contest_id}/"

    contest_page = requests.get(leetcode_constest_url)
    contest_data = contest_page.json()

    problem_ids = [question['question_id'] for question in contest_data['questions']]
    return problem_ids


def get_problem_by_slug(slug):
    url = "https://leetcode.com/graphql"
    params = {'operationName': "getQuestionDetail",
              'variables': {'titleSlug': slug},
              'query': '''query getQuestionDetail($titleSlug: String!) {
            question(titleSlug: $titleSlug) {
                questionId
                questionFrontendId
                questionTitle
                questionTitleSlug
                content
                difficulty
                stats
                similarQuestions
                categoryTitle
                topicTags {
                        name
                        slug
                }
            }
        }'''
              }

    json_data = json.dumps(params).encode('utf8')

    headers = {'User-Agent': user_agent, 'Connection':
        'keep-alive', 'Content-Type': 'application/json',
               'Referer': 'https://leetcode.com/problems/' + slug}
    resp = session.post(url, data=json_data, headers=headers, timeout=10)
    content = resp.json()

    # 题目详细信息
    question = content['data']['question']
    return question


def get_problems(problem_ids):
    url = "https://leetcode.com/api/problems/all/"

    resp = requests.get(url, timeout=10)
    if resp.status_code != 200:
        raise Exception('Cannot connect to Leetcode')

    question_list = json.loads(resp.content.decode('utf-8'))

    problem_len = 4
    problems = [0]*problem_len
    for question in question_list['stat_status_pairs']:
        if question['stat']['question_id'] in problem_ids:
            slug = question['stat']['question__title_slug']
            question_data = get_problem_by_slug(slug)

            title = question['stat']['question__title']
            url = f"https://leetcode.com/problems/{question['stat']['question__title_slug']}/"
            difficulty = question['difficulty']['level']

            content = BeautifulSoup(question_data['content'], 'html.parser')
            constraint = content.find_all('ul')[-1]

            question_id = question['stat']['frontend_question_id']

            problem_idx = problem_ids.index(question['stat']['question_id'])
            problems[problem_idx] = tuple([title, url, difficulty, constraint, question_id])

    return problems
