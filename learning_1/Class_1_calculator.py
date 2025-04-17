# input is the type of str
# use int around the invocation of input
"""
x = int(input("What's x?"))
y = int(input("What's y?"))

print(x + y)
"""
#the tinest type

#print(int(input("What's x?")) +int(input("What's y?")) )
'''
x = float(input("what's x?"))
y = float(input("what's y?"))
z = (x / y)
#print(f"{z:,}")
print(f"{z:.2f}")
'''
x,y = (input("What's number ? And what's the exponent ?").split(" "))
x = int(x)
y = int(y)
print(pow(x,y))