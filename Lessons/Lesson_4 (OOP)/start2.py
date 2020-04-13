import random
class Account:
    def __init__(self, number, size, currency):
        self.__number = number
        self.__size = size
        self.__currency = currency

        print("Constructor Working...")

    def __del__(self):
        print("Descructor working...")

    @property
    def number(self):
        return self.__number

    @property
    def size(self):
        return self.__size
    
    @property
    def currency(self):
        return self.__currency

    @size.setter
    def size(self, new_size):
        if new_size == 0:
            print("Error")
        else:
            self.__size = self.__size + new_size
    
    @size.setter
    def size(self, new_size):
        if new_size == 0:
            print("Error")
        else:
            self.__size = self.__size - new_size
            if self.__size < 0:
                print("you are not have money")


num = Account(random.randrange(100000, 999999), 100, "G" )
print('Номер рахунку => ', num.number)
num.size = 50
print('Розмір коштів => ', num.size)
print('Назва валюти рахунку => ', num.currency)


