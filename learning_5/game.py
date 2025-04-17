import random
def main():
    while True:
        try:
            num1 = int(input('Level: '))
        except ValueError:
            pass
        else:
            if num1 < 0:
                continue
            else:
                num2 = random.randint(0,num1)
                break
    while True:
        try:
            feedback = guess(num2, int(input('Guess: ')))
        except ValueError:
            pass
        else:
            if feedback == 'Just right!':
                print(feedback)
                break
            else:
                print(feedback)
def guess(x,gnum):
    if x == gnum:
        return 'Just right!'
    elif x < gnum:
        return 'Too large!'
    else:
        return 'Too small!'

if __name__ == '__main__':
    main()