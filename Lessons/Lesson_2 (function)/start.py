import random
import copy

# def sum():
#     print('function sum')
# sum()


# def sum(a, b):
#     print(a + b)
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# sum(a, b)


# def sum(a, b):
#     return a + b
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# res = sum(a, b)
# print("Result = ", res)


# def sum(*params):
#     res = 0
#     for item in params:
#         print(item)
#         res += item
#     return res

# result = sum(2, 5, 15)
# print('Result => ', result)


# tmp = 10
# i = 0
# for i in range(1, tmp, 2):
#     print(i)


# a = int(input("First number: "))
# b = int(input("Second number: "))

# def find_range(a,b):
#     res = 0
#     for i in range(a+1, b):
#         print('i = ', i)
#         res += i
#     return res

# result = find_range(a,b)
# print('Result => ', result)


# a = int(input("Введіть відстань пробігу: "))
# b = int(input("Введіть час пробігу: "))

# def sport(a,b):
#     return a/b
# res = sport(a,b)
# print('Середня швидкість => ', res)


# arr = [4, 6, 7, 8, 0, 9, 2, 4, 8, 8]
# # print(arr, 'type => ', type(arr))
# # for i in arr:
# #     print(i)
# print('========================>')
# # arr[2] = 100
# # for i in arr:
# #     print(i)

# arr.append(99)
# print('========================>')
# arr[2] = 100
# # for i in arr:
# #     print(i)
# print('========================>')
# arr.insert(2, 150)
# # for i in arr:
# #     print(i)

# arr.remove(4)
# print('========================>')
# for i in arr:
#     print(i)

# print("index => ", arr.index(0))
# print("Arr len => ", len(arr))
# print("count => ", arr.count(8))
# arr.pop()
# print("after pop => ")
# for i in arr:
#     print(i)

# print("Sort =================================>")
# arr.sort()
# for i in arr:
#     print(i)

# print("Revers =================================>")
# arr.reverse()
# for i in arr:
#     print(i)

# print("max => ", max(arr))
# print("min => ", min(arr))

# arr = [4, 6, 7, 8, [55, 43, 34], 66, 44, 'Works', True]
# print(arr)
# arr[4][1] = 90
# print(arr)


# person = ["Tom", "Bill", "Abram", "Steel", "Adam"]
# for i in person:
#     print(i)
# person.sort()
# for i in person:
#     print(i)


# a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# for i in range(len(a)):
#     a[i] = random.randint(-20, 30)
# print(a)
# for i in range(len(a)):
#     if a[i] < 0:
#         a[i] = -a[i]
# print(a)


# lang = ['C++', 'PYTHON', 'JavaScript', 'C#', 'Java', 'PHP', 'HTML', 'CSS']

# prog = lang
# print(prog)
# prog[0] = "Kotlin"
# print("Prog =>", prog)
# print("Lang =>", lang)


# prog = copy.deepcopy(lang)
# prog[0] = "Kotlin"
# print("Prog =>", prog)
# print("Lang =>", lang)


# part = lang[2:8:2]
# part = lang[:4]
# print(part)


# car = ('BMW', 'Renault', 'VW', 'Audi')
# print(car)
# for i in car:
#     print(i)

# print(car[-1])

# print(len(car))
# print("Audi count => ", car.count("Audi"))

# i = 0
# while i < len(car):
#     print(car[i])
#     i += 1

# person = ('Bill', 34)

# name, age = person
# print("Name : ", name, '\nAge : ', age)

# countries = {
#     "UA": "Ukraine",
#     "US": "USA",
#     "BR": "Brasil"
# }

# for key, value in countries.items():
#     print(key, "=====", value)

# countries.pop('BR')
# print('=======================AFTER============')
# for key, value in countries.items():
#     print(key, "=====", value)

# for key  in countries.keys():
#     print(key)

# for value in countries.values():
#     print(value)

# print(countries['UA'])
# print(countries.get("US"))

# countries["IT"] = "Italy"
# for key, value in countries.items():
#     print(key, "=====", value)

