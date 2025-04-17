
def main():
    name = input("Let's get adress of the name you mention,So What's the name?")
    if adress(name) == "no":
        print("We do not have ",gender(name),"'s adress")


def gender(n):
    g = {"Harry":"His","Hemiome":"Her"}
    return g.get(n,n)
def adress(n):
    a = {"Harry":"Room 1","Hemiome":"Room 2"}
    return a.get(n,"no")

main()
