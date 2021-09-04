#declaration
class Complex:
     def __init__(self, realpart, imagpart):
         self.r = realpart
         self.i = imagpart

x = Complex(6.0, -7.8)
print(x.r)
print(x.i)