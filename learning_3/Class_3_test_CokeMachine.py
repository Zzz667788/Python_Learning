def main():
    coke_machine()

# def coke(mon):#整体逻辑框架存在问题
#     print()
#     if  mon == 5 or 10 or 25:     #写法有问题
#         amount = 50 - mon
#         if amount <= 0:
#             return f"Change Owed: {amount}"
#         elif full > 0:
#             return f"Amount Due: {amount}\n" and

def coke_machine():
    amount = 50
    while amount > 0:
        mon = int(input(f"Amount Due: {amount}\n"
                +"Insert Coin: "))
        if mon == 5 or mon == 10 or mon == 25:
            amount -= mon
        else:
            continue
    print(f"Change Owed: {abs(amount)}")

if __name__ == '__main__':
    main()
