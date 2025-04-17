def main():
    name = input("camelCase: ")
    print(trans_name(name))

def trans_name(name):
    num = 0
    list = []
    newname = ""
    for i in name:              #for 后面 in跟着
        if i.isupper():         #issupper与isupper不同，前者表示整个字符串是否为大写字母，isupper用来检查单个字符是否大写
            list.append(num)
        num += 1
    # print(list)
    if list == []  :
        return name
    else:
        j = 0
        for i in list:
            if i == 0:
                continue
            name = "_".join([name[:(i + j)],name[(i + j):]])
            j += 1
            # print(name)
        name = name.lower()
        return name
if __name__ == '__main__':
    main()

# def trans_name(name):
#     new_name = ""
#     for i , char in enumerate(name):
#         if char.isupper() and i != 0:
#             new_name += "_" + char.lower()
#         else:
#             new_name += char.lower()
#     return new_name
# main()

