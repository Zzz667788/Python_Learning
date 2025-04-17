import sys
def main():
    names = []
    try:
        while True:
            name = input('Name: ')
            names.append(name)
    except EOFError:
        if len(names) == 0:
            return None
        else:
            print('Adieu, adieu, to',good_bye(names))

def good_bye(list):
     if len(list) == 1:
         return list[0]
     else:
         strings = ''
         for i,name in enumerate(list):
            if i <len(list) - 2:
                strings += name + ', '
            elif i == len(list) - 2:
                strings += name + ' and '
            else:
                strings += name
         return strings
if __name__ == '__main__':
    main()



