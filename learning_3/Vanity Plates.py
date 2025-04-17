def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(text):
    if text.isalnum() and 2<= len(text) <=6:
        num = 0
        for char in text:
            if char.isalpha():
                num += 1
            else:
                break
        if 2<= num:
            if num == len(text):
                return True
            elif int(text[num]) != 0:              #字符的个数=字符串第一个出现数字的序列，所以不需要+1
                 if text[num:].isnumeric():        #不需要再次遍历了
                    return True
            else:
                return False
    else:
        return False

if __name__ == '__main__':
    main()