from Just_setting_up_my_twttr import omitting

def test_shorten():
    text = ['a', 'ae', 'aei', 'aeiou']
    for i in text:
        assert omitting(i) == ''

if __name__ == '__main__':
    test_shorten()