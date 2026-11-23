import math
from random import choice

def circle_area(r):
    return math.pi * r ** 2

def square_area(s):
    return s ** 2

def rectangle_area(a,b): 
    return a * b

def triangle(a1,h):
    return 0.5 * a1 * h 

def main():

   # print ("Калькулятор геомтеричних фігур")

    print ("1. Коло")
    print ("2. Квадрат")
    print ("3. Прямокутник")

    choice = input("Оберіть Фігуру: ")
    if choice == "1":
        r = float(input("Радіус: "))
        print (f"Площа кола: {circle_area(r):.2f}")

    elif choice == "2":
        s = float(input("Сторона: "))
        print (f"Площа квадрата: {square_area(r):.2f}")

    elif choice == "3": 
        a = float(input("Перша Сторона:")) 
        b = float(input("Друга Сторона:")) 
        print (f"Площа прямокутника: {rectangle_area(a,b):.2f}")

if __name__ == "__main__":

    main()