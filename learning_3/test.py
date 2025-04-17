def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(text):
    if text.isalnum() and 2 <= len(text) <= 6:
        if text[:2].isalpha():
            has_digit = False
            for i, char in enumerate(text[2:]):
                if char.isdigit():
                    if i == 0 and char == '0':
                        return False
                    has_digit = True
                elif has_digit and char.isalpha():
                    return False
            return True
    return False

if __name__ == '__main__':
    main()