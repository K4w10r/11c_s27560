import math
import square_generator
# task 1

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squared_list = [i*i for i in list1]
print(list1)
print("task1: ", squared_list)

# task 2

def squared(start, end):
    res = []
    for i in range(start, end + 1):
        res.append(i**2)
    return res

print("task2: ", squared(1, 10))


# task 3

class MyClass:
    def class_squared(self, start, end):
        res = []
        for i in range(start, end + 1):
            res.append(i ** 2)
        return res

my_class = MyClass()
print("task3: ", my_class.class_squared(1, 10))

# task 4

library_list = [math.pow(i, 2) for i in list1]
print("task4: ", library_list)

# task 5
"""
class MyException(Exception):
    pass


class SquareGenerator:
    def sq_squared(self, start, end):
        if start < end:
            raise MyException("start should be greater than end")
        return squared(start, end)
"""

squared_generator = square_generator.SquareGenerator()
print("task5: ", squared_generator.sq_squared(3, 1))


# task 6

