def anwser(sth):
    return "Yes" if sth == "42" or sth =="forty-two" or sth =="forty two" else "No"

def main1():
    sth = input("What is the Answer to the Great Question of Life ,the Universe, and Everything ?")
    print(anwser(sth))
# main1()
def main2():
    greeting = input("Greeting:")
    print('$',output(greeting),sep="")
    print('$'+str(output(greeting)))
def output(Text):
    text = Text.lower()
    if text == "hello":
        return 0
    elif text[0] == "h":
        return 20
    else:
        return 100
# main2()
def main3():
    file_name = input("File name: ")
    print(file_type(file_name))
def file_type(n):
    if "." not in n:
        return "application/octet-stream"
    else:
        type = n.split(".")[-1]
        match type:
            case "gif":
                return "image/gif"
            case "jpg":
                return "image/jepg"
            case "png":
                return "image/png"
            case "pdf":
                return "application/pdf"
            case "txt":
                return "text/plain"
            case "zip":
                return "application/zip"
            case _:
                return "What?"
# main3()

def main4():
    ex = input("Expression: ")
    print(trans(ex))
def trans(ex):
    elements = ex.split(" ")
    num2 = float(elements.pop())    #pop是按照后进先出的原则一次弹出操作数和操作符的
    ope = elements.pop()
    num1 = float(elements.pop())
    match ope:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            return num1 / num2
        case _:
            return "Invalid operator"
# main4()

def main5():
    time = input("What time is it? ")
    print(convert(time),end="")
def convert(t):
    time = t.split(":")
    minutes = float(time[1])
    hours = float(time[0])
    if 0 <= hours <=24 and 0 <= minutes <=60:
        min = minutes/60
        if 7 <= hours < 8 or (hours == 8 and min == 0):
            return "breakfast time"
        elif 12 <= hours < 13 or (hours == 13 and min == 0):
            return "lunch time"
        elif 18 <= hours < 19 or (hours == 18 and min == 0):
            return "dinner time"
        else:
            return ""
    else:
        return "Wrong time!"
main5()


