'''def hello(to = "Darling!"):
    print("Hello,",to,"by the way, ",end="")
hello()

name = input("What's your name?")
hello(name)
'''
def hello(to = "new guy"):
    if to == "new guy":
        print("How are you doing?,", to, ",By the way,",end="")
        hello(input("What's your name?"))
    elif to =="" :
        print(hello(input("Er~~,Could you tell me your name please?")))
    else:
        print("Oh,Hello!",to,",Nice to see you!")
hello()
