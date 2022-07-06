# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# class Car :
#     x = 'something'
#     def __init__(self, height, width):
#         self.h = height
#         self.w = width
#     @classmethod
#     def get_area(cls):
#         print(cls.x)
#
#     @staticmethod
#     def get_some():
#         print('hello')
#
# # it = Car(4,5)
# Car.get_area()

li = [1,2,3,4,5,6,7,8,9,10]

def isOdd(n):
    return n % 2 == 1
def filterTest():
    new_li = list(filter(isOdd, li))
    filter_li = list(filter(lambda n: isOdd(n), li))
    print(new_li)
    print(filter_li)
    print(list(range(1,10)))

import collections
from collections import namedtuple, deque
def namedTuple():
    Point = namedtuple('Point', {'x':1, 'y':2})
    p = Point(1, 3)
    print(p)
    print(p._asdict())

# print(it.x)
def dequeutest():
    d = deque('abcdefg')
    # d.append('1')
    # print(d)
    d.appendleft('1')
    print(d)
    d.pop()
    print(d)
    d.popleft()
    print(d)
    # d.extend('123')
    # print(d)
    d.extendleft('123')
    print(d)
    d.rotate(2)
    print(d)
    d.rotate(-2)
    print(d)
    d = deque(range(10), maxlen=10)
    d.append(11)
    # d.appendleft(11)
    print(list(d))
    print(4<<1)
# d.clear()
# print(d)
def print_hi(name):
    for i in range (0,1):
    # Use a breakpoint in the code line below to debug your script.
        print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def test():
    squares = list(map(lambda x: x ** 2, range(10)))
    special_squares = list(filter(lambda x: x > 5 and x < 50, squares))
    print(special_squares)
    #
    # # (lambda x: print(x))([0,1,2,3])
    # # square = (lambda x: x**2)(range(10))
    names = ['Anne', 'Amy', 'Bob', 'David', 'Carrie', 'Barbara', 'Zach']

    b_names = list(filter(lambda s: s.startswith('B'), names))
    print (b_names)

def fibonacci(n):
    if(n<2): return 1;
    return fibonacci(n-1)  + fibonacci(n-2)

def outer(text):
    text = text.upper()
    def inner():
        print(text)
    return inner
func = outer('hello')

def loopTest():
    coefficient = [11,22,33,44,55,66,77,88,99]
    for index,coeff in  enumerate(coefficient[::-1]):
        print(index,coeff)

def arg_test(*arg):
    print(arg)

def kwarg_test(**data):
    print(data)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # func()
    arg_test(1,2,3,4)
    kwarg_test(name = 'trump', designation = 'president', country = 'usa', year = 2069)
    # fibonacci(10)
    # test()
    print_hi('PyCharm')



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
