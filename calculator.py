import math
from random import choice

def circle_area(r):
    return math.pi * r ** 2

def square_area(s):
    return s ** 2

def main():

   # print ("Калькулятор геомтеричних фігур")

    print ("1. Коло")
    print ("2. Квадрат")
    choice = input("Оберіть Фігуру: ")
    if choice == "1":
        r = float(input("Радіус: "))
        print (f"Площа кола: {circle_area(r):.2f}")

    elif choice == "2":
        s = float(input("Сторона: "))
        print (f"Площа квадрата: {square_area(r):.2f}")

if __name__ == "__main__":

    main()