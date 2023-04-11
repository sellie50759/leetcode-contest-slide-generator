#!/bin/bash
# generate leetcode contest slide and upload to hackmd
PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
export PATH

cd /home/azureuser/leetcode-contest-slide-generator/
source venv/bin/activate # 建立虛擬環境

contest_id="$(cat cron/weekly_contest_id)"
echo "weekly contest"
python3 main.py $contest_id

input_file="cron/weekly_contest_id" # 遞增contest_id
temp_file="temp.txt"

number=$(cat $input_file)
((number++))

echo $number > $temp_file
mv $temp_file $input_file


contest_id="$(cat cron/biweekly_contest_id)"
echo "biweekly contest"
python3 main.py -i 1 $contest_id
if [ $? -eq 0 ]; then
    input_file="cron/biweekly_contest_id" # 遞增contest_id
    temp_file="temp.txt"

    number=$(cat $input_file)
    ((number++))

    echo $number > $temp_file
    mv $temp_file $input_file
fi


if ls | grep "_slide.md$" > /dev/null ; then # 刪除產生的slide檔案
    rm *_slide.md
    echo "file deleted"
else
    echo "file doesn't exitst"
fi

exit 0
