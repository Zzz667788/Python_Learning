import sys

# print('My name is :',sys.argv[2])
# if __name__ == '__main__':

# if __name__ == '__main__': 是 Python 中常用的一种模块导入和执行的约定。这行代码的意思是：如果这个 Python 脚本是直接被运行的（而不是被导入到其他脚本中），那么就执行下面的代码块。
#
# 这种约定通常用于使一个 Python 文件既可以作为可执行脚本运行，又可以作为模块被其他脚本导入使用。具体来说：
#
# 当你直接运行一个 Python 文件时，Python 解释器会把这个文件的 __name__ 设置为 '__main__'，表示这个文件是主程序。
# 当你导入一个 Python 文件时，Python 解释器会把这个文件的 __name__ 设置为这个文件的模块名，表示这个文件是一个模块。
# 因此，通过在文件中使用 if __name__ == '__main__':，你可以编写一些在该文件作为主程序运行时才执行的代码，而在该文件被导入时不执行。这样可以使你的代码更具有灵活性和可重用性。
# a,b=[0,1]
# print(a,b)

# for i in  range(10):
#     print(i)

# i = '66,255.222'
# print(float(i.replace(',','')))

#requests测试

'''
import requests
import sys

respond = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
usd_rate = float(respond.json()['bpi']['USD']['rate'].replace(',', ''))

try:
    if len(sys.argv) == 1:
        print('Missing command-line argument')
        sys.exit()
    elif len(sys.argv) > 2:
        print('Too many arguments')
    else:
        num = float(sys.argv[1])
        print('$' + str(num * usd_rate))
except ValueError:
    print('Command-line argument is not a number')
'''

#test
# import pytest
#
# def test_division_by_zero():
#     with pytest.raises(ZeroDivisionError):
#         result = 1 / 0
# test_division_by_zero()

# def main():
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     X = True
#     while X:
#         text = input('Input: ')
#         num = len(text)
#         j = 0
#         for i in text:
#             j += 1
#             if i.lower() not in vowels:
#                 break
#             elif j == num:
#                 # shorten(text)
#                 print("X")
#                 X = False


# def shorten(word):
#     assert omitting(word) == ''


from Just_setting_up_my_twttr import omitting

def test_shorten():
    text = ['a', 'ae', 'aei', 'aeiou']
    for i in text:
        assert omitting(i) == ''

if __name__ == '__main__':
    test_shorten()