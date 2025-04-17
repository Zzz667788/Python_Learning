

def main():
    menu_machine()
def menu_machine():
    manu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    total = 0
    while True:
        try:
            total += float(manu[input("Item: ").title()])
        except :
            pass
        else:
            print(f'Total:${total:,.2f}')
    print("123")
main()