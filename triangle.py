__author__ = 'D15124888'

# Get user to input posiive values for a and o
a = 0
while a <= 0:
    a = float(input("Length of adjacent side: "))
o = 0
while o <= 0:
    o = float(input("Width of opposite side: "))

# calculate hypotenuse length
h = (a ** 2 + o ** 2) ** 0.5

# pint answer
print("")
print("The hypotenuse of a right-angle triangle with sides ", a, "and", o, "is", h)
