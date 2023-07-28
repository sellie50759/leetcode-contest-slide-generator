#!/bin/bash
# generate leetcode contest slide and upload to hackmd
PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
export PATH

cd /home/azureuser/leetcode-contest-slide-generator/
source venv/bin/activate # 建立虛擬環境

python3 main.py -1

python3 main.py -i 1 -1

if ls | grep "_slide.md$" > /dev/null ; then # 刪除產生的slide檔案
    rm *_slide.md
    echo "file deleted"
else
    echo "file doesn't exitst"
fi

exit 0
