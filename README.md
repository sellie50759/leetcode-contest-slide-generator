# leetcode-contest-slide-generator
automatic generate .md slide for leetcode weekly or biweekly contest

## Setup
python >= 3.9
1. git clone 到家目錄
2. ```python3 -m venv venv && source tutorial-env/bin/activate``` 安裝並進入虛擬環境
3. ```pip3 install -r requirements.txt``` 安裝相依套件
4. 在 utils/settings.py 裡填上對應的 hackmd api key 與團隊名稱
      * 取得 hackmd api key 看[這篇](https://hackmd.io/@docs/HackMD_API_Book/https%3A%2F%2Fhackmd.io%2F%40hackmd-api%2Fdeveloper-portal)
      * 團隊名稱在 hackmd 團隊首頁 /team/{團隊名稱}
## 手動使用
使用```python3 main.py -h```查看相關設定 
## crontab腳本設定
1. ```crontab -e``` 打開 crontab 介面
2. 將 crontab 裡的腳本更改成對應本機的正確時區
    * 查看 ubuntu 本機時區 ```timedatectl```
    * 本機時區 UTC +0，對應的腳本為 ```0 6 * * 0 ~/leetcode-contest-slide-generator/cron/cron.sh```
    * 本機時區 UTC +8，對應的腳本為 ```0 14 * * 0 ~/leetcode-contest-slide-generator/cron/cron.sh```
4. 將腳本改成可執行 ```chmod +x ~/leetcode-contest-slide-generator/cron/cron.sh```
