"""this code is meant to do some calculations"""
import math


def golden_ratio():
    """this function prints the value of the golden ratio"""
    print((1+math.sqrt(5))/2)


def six_cubed():
    """a function that prints the value of 6 cubed"""
    print(math.pow(6, 3))


def hypotenuse():
    """a function that prints the length of the hypotenuse of
    a straight-angled triangle whose ribs are 3 and 5"""
    print(math.sqrt(3**2+5**2))


def pi():
    """a function that prints the value of the constant: pi"""
    print(math.pi)


def e():
    """a function that prints the value of the constant: e"""
    print(math.e)


def triangular_area():
    """a function that prints the areas of straight-angled
    and isosceles triangles, with a rib of 1-10"""
    print(1/2, 2**2/2, 3**2/2, 4**2/2, 5**2/2,
          6**2/2, 7**2/2, 8**2/2, 9**2/2, 10**2/2)


if __name__ == "__main__" :
    golden_ratio()
    six_cubed()
    hypotenuse()
    pi()
    e()
    triangular_area()