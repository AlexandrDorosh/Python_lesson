import random
# 1
# question = int(input('what time is it (24): '))

# if question > 0 and question < 6:
#     print("Good night")
# elif question >= 6 and question < 12:
#     print("Good morning")
# elif question >= 12 and question < 18:
#     print("Good day")
# elif question >= 18 and question < 24:
#     print("Good evening")
# elif question == 24:
#     print("Good night")
# else:
#     print("Error!!! Enter numbers in the range 1-24")


# 2
# exit = False
# while not exit:
#     choice = int(input('1. Сантиметри \n2. Дюйми \n0. Вийти\n==> '))
#     if choice == 1:
#         choice2 = int(input('1. Ввести сантиметри які потрібно перевести в дюйми\n0. Вийти\n==> '))
#         if choice2 == 1:
#             CM = int(input('Введіть см : '))
#             print(CM / 2.54, 'Дюйми')
#         elif choice2 == 0:
#             exit = True
#     if choice == 2:
#         choice2 = int(input('1. Ввести дюйми які потрібно перевести в сантиметри\n0. Вийти\n==> '))
#         if choice2 == 1:
#             inches = int(input('Введіть дюйми : '))
#             print(inches * 2.54, 'См')
#         elif choice2 == 0:
#             exit = True
#     elif choice == 0:
#         exit = True


# 3
# exit = False
# while not exit:
#     choice = int(input('1. Цельсій \n2. Фаренгейт \n0. Вийти\n==> '))
#     if choice == 1:
#         choice2 = int(input('1. Введіть градус Цельсій який потрібно перевести в Фаренгейти\n0. Вийти\n==> '))
#         if choice2 == 1:
#             TC = int(input('Введіть число: '))
#             print(TC * 1.8 + 32, 'Фаренгейтів')
#         elif choice2 == 0:
#             exit = True
#     if choice == 2:
#         choice2 = int(input('1. Введіть градус Фаренгейта який потрібно перевести в Цельсій\n0. Вийти\n==> '))
#         if choice2 == 1:
#             TF = int(input('Введіть число: '))
#             print((TF - 32) * 5 / 9, 'Цельсій')
#         elif choice2 == 0:
#             exit = True
#     elif choice == 0:
#         exit = True


# 4
# num = 0
# mult = 1
# add = 0
# while num < 8:
#     number = int(input('Введіть число: '))
#     num +=1
#     mult = number * mult
#     add = number + add
#     div = add / 8
# print(mult, '- Добуток чисел, ', div, '- Середнє арифметичне')


# 5
# i = 0
# while i < 7:
#     temp = random.randrange(-10, 30)
#     print(temp)
#     if i == 0:
#         min = temp
#         max = temp
#     if temp < min:
#         min = temp
#     if temp > max:
#         max = temp
#     i += 1
# print('MIN NUMBER ==> ', min)
# print('MAX NUMBER ==> ', max)
