from collections import Counter
import sys

def main():
    count_items()

def count_items():
    items = []
    try:
        while True:
            try:
                items.append(input(":").upper())
            except ValueError:
                pass
    except (EOFError, KeyboardInterrupt):
        pass

    counter = Counter(items)
    for string, count in sorted(counter.items()):
        print(count, string)

main()