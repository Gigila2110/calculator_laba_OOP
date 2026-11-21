import math
from random import choice

def circle_area(r):
    return math.pi * r ** 2

def main():

   # print ("Калькулятор геомтеричних фігур")

    print ("1. Коло")
    choice = input("Оберіть Фігуру: ")
    if choice == "1":
        r = float(input("Радіус: "))
        print (f"Площа кола: {circle_area(r):.2f}")

if __name__ == "__main__":

    main()