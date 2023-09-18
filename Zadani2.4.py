import math 

try:
    a = int(input("Zadej hodnotu a: "))
    b = int(input("Zadej hodnotu b: "))
    c = int(input("Zadej hodnotu c: "))

    discriminator = b**2 - 4*a*c

    if discriminator >= 0:
        x1 = (-b + math.sqrt(discriminator)) / 2 * (a)
        x2 = (-b - math.sqrt(discriminator)) / 2 * (a)