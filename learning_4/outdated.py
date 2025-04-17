import re
from datetime import datetime
def main():
    outdate()
def outdate():
    list = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    month_dict = {month : index + 1 for index,month in enumerate(list)}  #字典推导式
    while True:
        date = input('Date: ')
        pattern1 = r'^(\d{1,2})/(\d{1,2}/(\d{1,4}))$' #{}中只能包含两个数字，表示前面的元素重复的次数范围\d{1,4}表示匹配一个数字，重复次数为1到4此
        # pattern1 = r'^(\d+/\d+/\d+)'
        pattern2 = r'^(\w+) (\d{1,2}),(\d{1,4})$'
        # pattern2 = r'^(\w+ \d+,\d+)'
        try:
            if re.match(pattern1,date):
                month,day,year = map(int,re.findall(r'\d+',date))
                datetime(year,month,day)    #检查日期合理性
                print(f'{year}-{month:02d}-{day:02d}')
                break
            elif re.match(pattern2,date):
                date = re.findall(r'\w+',date)
                if date[0].capitalize() in month_dict:
                    month = int(month_dict.get(date[0].capitalize()))
                    datetime(int(date[2]),month,int(date[1]))
                    print(f'{int(date[2])}-{int(date[1]):02d}-{month:02d}')
                    # print(f'{int(date[2])}-{int(date[1]):02d}-{int(month_dict.get(date[0],'')):02d}')
                    break
                else:
                    continue
            else:
                continue
        except ValueError:
            pass
main()