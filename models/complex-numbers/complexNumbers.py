"""
The following code presents a pure implementation of complex numbers in python
"""
import math


class Complex(object):
    """
    Complex number object model
    """

    @staticmethod
    def complexArgument(re, im):
        """
        The following function is used by the name of 'atan2'
        A function to calculate complex number argument in the proper quadrant
        """
        if re > 0:
            return math.atan(im / re)
        elif re < 0:
            if im >= 0:
                return math.atan(im / re) + math.pi
            else:
                return math.atan(im / re) - math.pi
        else:
            if im > 0:
                return math.pi / 2
            elif im < 0:
                return -1 * math.pi / 2

    @staticmethod
    def complexModulus(re, im):
        """
        The following function calculates |z| with given real and imaginary part of a complex number z
        """
        return math.sqrt(re**2+im**2)

    def __init__(self, real=None, imaginary=None, radius=None, angle=None):
        """
        Define a complex number through its base form
        Define either through:
        - Giving real and imaginary
        - Giving radius and angle
        """
        if real is not None and imaginary is not None:
            self.real = real
            self.imaginary = imaginary
            self.radius = math.sqrt(self.real ** 2 + self.imaginary ** 2)
            self.angle = Complex.complexArgument(self.real, self.imaginary)
        elif radius is not None and angle is not None:
            self.radius = radius
            self.angle = angle
            self.real = self.radius * math.cos(self.angle)
            self.imaginary = self.radius * math.sin(self.angle)
        else:
            raise ValueError(
                "Complex number constructor failed. Use either real and imaginary or radius and angle data")

    def __add__(self, other):
        if type(other) is Complex:
            return Complex(self.real + other.real, self.imaginary + other.imaginary)
        elif type(other) is float or type(other) is int:
            return Complex(self.real + other, self.imaginary)
        else:
            raise TypeError(f"Unsupported operand type(s) for +: <class 'Complex'> and {type(other)}")

    def __sub__(self, other):
        if type(other) is Complex:
            return Complex(self.real - other.real, self.imaginary - other.imaginary)
        elif type(other) is float or type(other) is int:
            return Complex(self.real - other, self.imaginary)
        else:
            raise TypeError(f"Unsupported operand type(s) for -: <class 'Complex'> and {type(other)}")

    def __mul__(self, other):
        if type(other) is Complex:
            return Complex(radius=self.radius * other.radius, angle=self.angle + other.angle)
        elif type(other) is float or type(other) is int:
            return Complex(self.real * other, self.imaginary * other)
        else:
            raise TypeError(f"Unsupported operand type(s) for *: <class 'Complex'> and {type(other)}")

    def __truediv__(self, other):
        if type(other) is Complex:
            return Complex(radius=self.radius / other.radius, angle=self.angle - other.angle)
        elif type(other) is float or type(other) is int:
            return Complex(self.real / other, self.imaginary / other)
        else:
            raise TypeError(f"Unsupported operand type(s) for /: <class 'Complex'> and {type(other)}")

    def __repr__(self):
        """
        The function returns a string (base) version of a complex number
        Very sophisticated and unintentionally prolonged function to compensate float approximation error
        Probably wrong as well
        """
        float_error = 2
        if round(self.real, float_error) == 0:
            return f"{round(self.imaginary, float_error)}i"
        if round(self.imaginary, float_error) == 0:
            return str(round(self.real, float_error))
        return f"{round(self.real, float_error)}+{round(self.imaginary, float_error)}i"


# print(Complex(1, 2) - 1)
# print(Complex(1, 1) * Complex(1, 1))
# print(Complex(1, 1) / Complex(1, 1))
