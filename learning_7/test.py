# num = ['1','2']
# a,b,c = num
# print(f'a is {a},b is {b},c is {c}')
#
import csv

students = [{'name' : 'a','num':'1'},{'name' : 'b','num':'2'}]
student = {}
student['name'] = 'Z'
student['house'] = 'X'
students.append(student)
print(students)
print(type(students))

def get_house(student):
    return student['house']
for student in sorted(students,key=get_house):
    print()
    '''
    当 sorted() 函数调用时，它会对 students 列表中的每个字典元素进行排序。在排序过程中，对于每个字典元素，get_house 函数会被调用，并将当前的字典元素作为参数传递给它。然后，get_house 函数会返回该字典元素中 'house' 键对应的值（即学生所在的房子），以便 sorted() 函数根据这个值来排序字典元素。

整个过程可以这样理解：

对于第一个字典 {'name': 'a', 'house': '1'}，get_house 函数被调用，并传递这个字典作为参数。get_house 函数返回 '1'。
对于第二个字典 {'name': 'b', 'house': '2'}，同样地，get_house 函数被调用，并传递这个字典作为参数。get_house 函数返回 '2'。
最终，sorted() 函数根据 get_house 函数返回的值对这两个字典元素进行排序，得到一个按照 'house' 键的值升序排列的列表。
    '''
# students = []
# with open('a.csv') as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append(row)

# import sys
# from PIL import Image
# images = []
#
# for arg in sys.argv:
#     image = Image.open(arg)
#     images.append(image)
#
# images[0].save(
#
# )