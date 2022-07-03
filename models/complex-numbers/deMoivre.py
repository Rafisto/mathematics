"""
The following code uses de Moivre Theorem to solve simple equations
"""
import math

from complexNumbers import Complex


class DeMoivreEquation(object):
    """
    Class to store every equation of the form z^n=k, where z in C, k in C, n in Z
    """

    def __init__(self, n, k):
        self.n = n
        self.k = k
        self.assertTypes()
        self.solutions = self.Solve()

    def assertTypes(self):
        """
        Check whether given parameters are correct by type
        """
        assert type(self.n) == float or type(self.n) == int
        assert type(self.k) == Complex

    def Solve(self):
        """
        A simple algorithm to solve de Moivre equation
        """
        radius = Complex.complexModulus(self.k.real, self.k.imaginary)
        angle = Complex.complexArgument(self.k.real, self.k.imaginary)
        solutions = []
        for k in range(self.n):
            phase = (angle + 2 * k * math.pi) / self.n
            solutions.append(Complex(real=radius ** (1 / self.n) * math.cos(phase),
                                     imaginary=radius ** (1 / self.n) * math.sin(phase)))
        return solutions

    def __repr__(self):
        return f"z^{self.n}={self.k} has {self.n} solutions: {'; '.join([str(s) for s in self.solutions])}". \
            replace("+-", "-")


print(DeMoivreEquation(n=3, k=Complex(-8, 0)))
print(DeMoivreEquation(n=6, k=Complex(-64, 0)))
