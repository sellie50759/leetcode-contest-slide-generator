# leetcode-contest-slide-generator
automatic generate .md slide for leetcode weekly or biweekly contest

## Setup
python >= 3.9
1. git clone 到家目錄
2. ```python3 -m venv venv && source tutorial-env/bin/activate``` 安裝並進入虛擬環境
3. ```pip3 install -r requirements.txt``` 安裝相依套件
4. 在 utils/settings.py 裡新增 hackmd api key 與團隊名稱
## 手動使用
使用```python3 main.py -h```查看相關設定 
## crontab腳本設定
1. 將 crontab 裡的時間更改成對應你本機的正確時間
    * 本機時間 UTC +0，對應的腳本為 ```0 6 * * 0 ~/leetcode-contest-slide-generator/cron/cron.sh```
    * 本機時間 UTC +8，對應的腳本為 ```0 14 * * 0 ~/leetcode-contest-slide-generator/cron/cron.sh```
2. 將腳本改成可執行 ```chmod +x ~/leetcode-contest-slide-generator/cron/cron.sh```
