import sys
import pyfiglet
import random
def main():
    for i in range(3):
        text = input("Input:")
        print('Output:', trans_font(text),sep="\n")
def trans_font(string):
    if len(sys.argv) == 1:
        all_fonts = pyfiglet.FigletFont.getFonts()
        random_font = random.choice(all_fonts)
        return pyfiglet.figlet_format(string,font=random_font)
    elif len(sys.argv) == 3:
        try:
            if sys.argv[1] == '-f' or sys.argv[1] == '--font':
                return pyfiglet.figlet_format(string,font=sys.argv[2])
        except:
            sys.exit()
    else:
        sys.exit()

if __name__ == '__main__':
    main()

