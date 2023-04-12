# leetcode-contest-slide-generator
automatic generate .md slide for leetcode weekly or biweekly contest

## Setup
1. ```python3 -m venv venv && source tutorial-env/bin/activate``` 安裝並進入虛擬環境
2. ```pip3 install -r requirements.txt``` 安裝相依套件
3. 在 utils/settings.py 裡新增hackmd api key與團隊名稱
## 手動使用
使用```python3 main.py -h```查看相關設定 
## crontab腳本設定
1. ```crontab -e``` 將 cron/crontab_script 的內容貼到裡面
2. 將 cron/weekly_contest_id 與 cron/biweekly_contest_id 更新成周賽與雙周賽對應的最新id
