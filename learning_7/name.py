# name = input('What your name ?')
#
# file = open('name.txt','a')
# file.write(f'{name}\n')
# file.close()

with open('name.txt','r')as file:
    lines = file.readlines()
print(type(lines))
for name in lines:
    print(name,end='')