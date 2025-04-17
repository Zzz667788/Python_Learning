import sys

def main():
    print(validate(input("IPv4 Address: ")))
def validate(ad):
    nums = ad.strip().split('.')
    answer = True
    if len(nums) == 4:
        for num in nums:
            try:
                if 0 < int(num) < 255:
                    continue
                else:
                    answer = False
            except ValueError:
                answer = False
                sys.exit()
    else:
        answer = False
    print(type(nums), nums)
    return answer
if __name__ == "__main__":
    main()