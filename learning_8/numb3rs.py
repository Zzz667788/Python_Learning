import sys
import re
def main():
    print(validate(input("IPv4 Address: ")))

def validate(address):
    '''nums = ad.strip().split('.')
    answer = True
    if len(nums) == 4:
        for num in nums:
            try:
                if 0 <= int(num) <= 255:
                    continue
                else:
                    answer = False
                    break
            except ValueError:
                answer = False
                sys.exit()
    else:
        answer = False
    print(type(nums), nums)
    return answer


    '''
    '''
    answer = True
    if matches := re.search(r'^(\d+)\.(\d+)\.(\d+)\.(\d+)$',address):
        try:
            for i in range(4):
                if 0 <= int(matches.group(i+1)) <= 255:
                    continue
                else:
                    return False
        except ValueError:
            return False
        # except AttributeError:
        #     return False
        else:
            return answer
            # print(type(matches.groups()),matches.groups())
    else:
        return False
'''
    patren = r'^(\d{0,3}+)\.(\d{0,3}+)\.(\d{0,3}+)\.(\d{0,3}+)\.$'
    if not re.match(patren,address):
        return False
    parts = address.split('.')
    for part in parts:
        if not 0 <= part <= 255:
            return False

if __name__ == "__main__":
    main()