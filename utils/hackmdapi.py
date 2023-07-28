from utils.settings import HACKMD_API_KEY, TEAM_PATH
import requests
team_url = f'https://api.hackmd.io/v1/teams/{TEAM_PATH}/notes'
headers = {'Authorization': f'Bearer {HACKMD_API_KEY}'}


def getTeamNotes():
    r = requests.get(team_url, headers=headers)
    team_notes = r.json()

    return team_notes


def readNote(note_path):
    with open(note_path, 'r') as f:
        return f.read()


def uploadNote(note_path):
    post_data = {
        "title": "",
        "content": readNote(note_path),
        "readPermission": "guest",
        "writePermission": "owner",
        "commentPermission": "everyone"
    }

    r = requests.post(team_url, json=post_data, headers=headers)
    if r.status_code != 201:
        raise Exception('upload note fail')


if __name__ == '__main__':
    uploadNote("test.md")
