
def main():
    name = input("What's the name?")
    if adress(name) == "not":
        print("We don't have ",name,"'s adress")
    else:
        print(name,"'s adress is ",adress(name))

def adress(n):
    t = n.lower()
    a = {"herry":"room 1","heriomy":"room2"}
    return a.get(t,"not")
main()
