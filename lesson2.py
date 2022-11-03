# legb scope

# local -l
# enclosed
# global - g
# built-in -b


a = "global var"

# def get_sum():
#     a = 4
#     b = 5
#     return a + b
# print(get_sum())
# print(a)


# pi = 3.15
# def get_pi():
#     global pi
#     pi = 3.11
#     print(pi)
#
# get_pi()
# print(pi)


# def get_pi():
#     pi = 3.11
#     print(pi)
#
# func = get_pi
# func()


def obertka(func):
    def _wrapper():
       print("f")
def get_pi():
    pi = 3.11
    print(pi)
