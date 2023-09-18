import math

#Metoda vypoctu obsahu
def calculate_content(radius):
    if radius <= 0:
        raise ArithmeticError("Polomer musi byt kladne cislo")
    content = math.pi * (radius ** 2)
    return content

try:
    radius = int(input("Zadej polomer: "))
    content = calculate_content(radius)
    print(f"Obsah kruhu je {content}")
except ValueError:
    print("Byly zadane neplatne hodnoty")
except ArithmeticError as e:
    print(e)
