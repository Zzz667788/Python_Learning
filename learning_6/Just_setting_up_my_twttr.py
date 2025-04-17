def main():
    text = input("Input: ")
    print("Output:",omitting(text))

# def omitting(str):
#     new_str = ''              #修改字符串可以找新的字符串保存修改后的结果
#     for char in str:
#         if char.lower() == 'a'or char.lower() =='e' or char.lower() == 'i' or char.lower() == 'o' or char.lower() == 'u':
#             new_str += ''       #原来使用replace（）并没有真正并没有真正地替换掉字符串中的元音字母，因为字符串是不可变对象，在 Python 中无法直接修改字符串的某个字符。replace() 方法会返回一个新的字符串，但不会修改原始字符串。
#         else:                    #可以使用一个新的字符串来保存结果，并在循环中将非元音字母添加到这个新字符串中
#             new_str += char
#     return new_str
def omitting(text):
    vowels = 'aeiou'
    new_text = ''
    for char in text:
        if char.lower() not in vowels:
            new_text += char
        else:
            continue
    return new_text

if __name__ == '__main__':
    main()