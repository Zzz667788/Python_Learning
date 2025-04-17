from collections import Counter
import sys

def main():
    count_items()

def count_items():
    items = []
    try:
        while True:
            try:
                items.append(input(""))
            except ValueError:
                pass
    except EOFError:
        pass
    except KeyboardInterrupt:
        pass
    counter = Counter(items)
    for strings,i in sorted(counter.items()):
        print(i,strings.upper())
main()