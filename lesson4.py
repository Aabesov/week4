# files

# open()

# r = read

# file = open("test.txt", "r")
# print(file.read())
# print(file.readline())
# print(file.readlines())

# w write
# file = open("test.txt", "w")
# file.write("Helllo")
# file.close()


# file = open("rannge.txt", "w")
# counter = 11
# for i in range(1, 1000001):
#     if i == counter:
#         counter += 10
#         file.write(f"\n{i} ")
#     else:
#          file.write(f"{i} ")
#
# file.close()


file = open("numm.txt", "w")
counter = 11
for i in range(1, 101):
    if i == counter:
        counter += 10
        file.write(f"\n{i} ")
    else:
         file.write(f"{i} ")

file.close()

file = open("numm.txt", "r+")
for i in file:
    if i % 2 == 0:
        a = i * 2
        print(a)

    # print(a.split(" "))


# with open("test.txt", "a") as file:


