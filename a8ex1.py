"""
Author: Oleh Karavskyi
Matr.Nr.: k12139895
Exercise: 1
"""

class Complex:

    def __init__(self, real: float, imaginary: float):

        if isinstance(real, int):
            self.real = int(real)
        if isinstance(real, float):
            self.real = float(real)
        if isinstance(imaginary, int):
            self.imaginary = int(imaginary)
        if isinstance(imaginary, float):
            self.imaginary = float(imaginary)

    def __eq__(self, other):
        if isinstance(other, Complex):
            return self.real == other.real and self.imaginary == other.imaginary
        return NotImplemented

    def __repr__(self):
        return f"Complex(real={self.real}, imaginary={self.imaginary})"

    def __str__(self):

        if self.imaginary < 0:
            return f"{self.real} - {self.imaginary*-1}i"
        else:
            return f"{self.real} + {self.imaginary}i"

    def __abs__(self):

        return (self.real**2 + self.imaginary**2)**0.5

    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real + other.real, self.imaginary + other.imaginary)
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Complex):
            self.real += other.real
            self.imaginary += other.imaginary

            return Complex(self.real, self.imaginary)
        return NotImplemented


    @staticmethod
    def add_all(comp: "Complex", *comps: "Complex") -> "Complex":

        if isinstance(comp, Complex):
            multi_c = Complex(comp.real, comp.imaginary)
            for c in comps:
                multi_c.real += c.real
                multi_c.imaginary += c.imaginary

        return multi_c

