import math
def Triangle(a,b,c):
    if a+b > c and a+c > b and b+c > a:
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            return "c'est un triangle rectangle"
        elif a == b and b == c:
            return "C'est un triangle équilatéral"
        elif a == b or a == c or b == c:
            if a**2 + b**2 == int(c**2) or a**2 + int(c**2) == b**2 or b**2 + int(c**2) == a ** 2:
                return "C'est un triangle rectangle isocèle"
            else:
                return "C'est un triangle isocèle"
        else:
            return "C'est un triangle quelconque"


print(Triangle(3, 4, 5))
print(Triangle(3, 3, 3))
print(Triangle(3, 3, 2))
print(Triangle(1, 1, math.sqrt(2)))
print(Triangle(3, 4, 6))