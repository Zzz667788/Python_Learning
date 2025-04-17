import random
def main():
    generate_integer(get_level())
def get_level():
    while True:
        try:
            level = int(input('Level:'))
        except ValueError:
            pass
        else:
            if 1 <= level <= 3:
                return level
            else:
                continue
def generate_integer(lev):
    '''
    if lev == 1:
        ran1 = 0
        ran2 = 9
    elif lev == 2:
        ran1 = 10
        ran2 = 99
    else:
        ran1 = 100
        ran2 = 999
    '''
    level_range = {
        1:(0,9),
        2:(10,99),
        3:(100,999)
    }
    ran1,ran2 = level_range.get(lev,(0,0))
    score = 0
    for i in range(10):
        num = 0
        x = random.randint(ran1,ran2)
        y = random.randint(ran1,ran2)
        z = x + y
        while True:
            try:
                if num < 3:
                    answer = int(input(f'{x} + {y} = '))
                else:
                    print(f'{x} + {y} = {z}')
                    break
            except ValueError:
                print('EEE')
                num += 1
            else:
                if answer == z:
                    score += 1
                    break
                else:
                    print('EEE')
                    num += 1
    print('Score:',score)
if __name__ == '__main__':
    main()