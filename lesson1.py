# dict comprehetion


# kpi = {
#     "math": [2, 4, 6, 7],
#     "py": [2, 33, 6, 87],
#     "java": [2, 55, 6, 77],
# }
# dict_number = {key: sum(value) for key, value in kpi.items()}
# print(dict_number)


# kpi = {
#     "math": [2, 4, 6, 7],
#     "py": [2, 33, 6, 87],
#     "java": [2, 55, 6, 77],
# }
# dict_number = {key: sum(value) if sum(value) != 128 else None for key, value in kpi.items() if sum(value) > 50}
# print(dict_number)]


# map

# list_rad = [12, 33, 45, 6]
# def get_square_circle(rad):
#     from math import pi
#     square = pi * rad**2
#     return round(square, 2)
# list_square = list(map(get_square_circle, list_rad))
# print(list_square)


# list_num = [5, 6, 3, 9, 3]
# def get_factorial(fact):
#     factorial = 1
#     for i in range(1, fact + 1):
#         factorial = factorial * i
#     return factorial
#
# list_fact = list(map(get_factorial, list_num))
# print(list_fact)


# def sum_num(a, b):
#     return a + b
#
# list_num1 = [2, 4, 6, 8]
# list_num2 = [1, 3, 5, 7]
# sum_list = list(map(sum_num, list_num1, list_num2))
# print(sum_list)

# filter

# list_number = [22, 32, 42, 6, 15, 64]
# def get_divided_num(a):
#     if a % 2 == 0:
#         return a
# list_divided_num = list(filter(get_divided_num, list_number))
# print(list_divided_num)


# names = ["Aimarjan", "Kudaiberdi", "Arsen", "Aidana"]
# def get_names(a):
#     if len(a)>= 7:
#         return a
# list_names = list(filter(get_names, names))
# print(list_names)



# names1 = ["Aimarjan", "Kudaiberdi", "Arsen", "Aidana"]
# names2 = ["Aimarjan", "Nurlan", "John", "Tom"]
# new_list = []
# def compare_names(a, b):
#     if a == b:
#         return a
#
#
# list_names = list(filter(lambda x: x is not None, list(map(compare_names, names1, names2))))
# print(list_names)



# from functools import reduce
# list_num = [12, 2, 3, 5, 7, 5, 19]
# def get_multiple_int(num1, num2):
#     return num1 * num2
# multiple_int = reduce(get_multiple_int, list_num)
# print(multiple_int)


def make_humburger(func):
    def wrapper():
        print("Up bread")
        print("Sous")
        func()
        print("Sous")
        print("Sub bread")
    return wrapper

def make_beef():
    print("beef ham")

def make_chiken():
    print("Chiken ham")


