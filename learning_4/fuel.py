def main():
    print(fuelgauge())

def fuelgauge():
    while True:
        text = input("Fraction: ")
        if '/' not in text:
                continue
        else:
            x,y = text.split('/')
        try:
            if int(x) > int(y) or int(y) == 0:
                continue
        except ValueError:
            pass
        else:
            fra = int(int(x)/int(y)*100)
            if 1 < fra < 99:
                return f'Fraction: {fra}%'
            elif fra <= 1:
                return 'E'
            else:
                return 'F'

main()