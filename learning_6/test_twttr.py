from Just_setting_up_my_twttr import omitting

def main():
    test_shorten()
    # vowels = ['a','e','i','o','u']
    # X = True
    # while X:
    #     text = input('Input: ')
    #     num = len(text)
    #     j = 0
    #     for i in text:
    #         j += 1
    #         if i.lower() not in vowels:
    #             break
    #         elif j == num:
    #
    #             X =

def test_shorten():
    text = ['a', 'ae', 'aei', 'aeiou']
    for i in text:
        assert omitting(i) == ''

if __name__ == '__main__':
    main()
