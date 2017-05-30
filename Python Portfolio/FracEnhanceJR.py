######################################################################################################################
# Name: Jacob Ryans
# Date: 2/24/17
# Description: Fraction calculation program
######################################################################################################################

class Fraction(object):
    
        def __init__(self, num = 0, den = 1):
            self.num = num
            # Make sure not to set the denominator to 0 if specified
            if (den == 0):
                den = 1
            self.den = den

        @property
        def num(self):
            return self._num

        @num.setter
        def num(self, value):
            self._num = value

        @property
        def den(self):
            return self._den

        @den.setter
        def den(self,value):
            if (value != 0):
                self._den = value

        def getReal(self):
            a = float(self.num) / self.den
            return a

        def __add__(self, other):
            sumnum = (self.num * other.den) + (other.num * self.den)
            sumden = self.den * other.den
            summ = Fraction(sumnum, sumden)

            return summ

        def __sub__(self, other):
            subnum = (self.num * other.den) - (other.num * self.den)
            subden = self.den * other.den
            diff = Fraction(subnum, subden)

            return diff

        def __mul__(self, other):
            mulnum = self.num * other.num
            mulden = self.den * other.den
            prod = Fraction(mulnum, mulden)

            return prod
    
        def __div__(self, other):
            divnum = self.num * other.den
            divden = self.den * other.num
            quot = Fraction(divnum, divden)

            return quot

        def __str__(self):
            return "{}/{} ({})".format(self.num, self.den, self.getReal())

        def reduce(self):
            gcd = 1
            # Assume the smaller is the numerator
            minn = self.num

            if (self.den < self.num):
                    minn - self.den

            for i in range(2, minn + 1):
            # When we find one, update the GCD
                    if (self.num % i == 0 and self.den % i == 0):
                        gcd = i

            # Divide the numerator and denominator by the GCD
            self.num /= gcd
            self.num /= gcd

            # If the numerator is 0, set the denominator to 1
            if (self.num == 0):
                    self.den = 1

                # Calculates and returns the sum of two fraction
    
                

# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# the main part of the program
# create some fractions
f1 = Fraction(1, 1)
f2 = Fraction(5, 8)
f3 = Fraction(3, 4)
f4 = Fraction(1, 0)

# display them
print f1
print f2
print f3
print f4

# play around
f3.num = 5
f3.den = 8
f1 = f2 + f3
f4.den = 88
f2 = f1 - f1
f3 = f1 * f1
f4 = f4 / f3

# display them again
print f1
print f2
print f3
print f4
