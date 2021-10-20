import cmath


class ComplexNumber:
    """
    A class representing complex number
    """

    def __init__(self, real, imag=0.0):
        self.real = real
        self.imag = imag

    @classmethod
    def from_string(cls, number_as_str):
        """
        Alternative constructor for ComplexNumber class. It accepts complex number as a string, for example '2.1+4.2j'
        and creates a ComplexNumber object
        """
        new_str = None
        sign = None
        signs = ['+', '-']
        for idx, char in enumerate(number_as_str):
            if char in signs:
                sign = number_as_str[idx]
                new_str = number_as_str.replace(sign, " ")
                break

        if new_str is None or sign is None:
            raise RuntimeError("Incorrect string has been passed to the constructor of ComplexNumber class")
        else:
            real, imag = new_str.split()
            imag = imag[:-1]
            real, imag = float(real), float(imag)
            imag = imag if sign == '+' else -imag
            return cls(real, imag)

    def __repr__(self):
        return f"({self.real}{'+' if self.imag >= 0 else '-'}{abs(self.imag)}j)"

    def __add__(self, other):
        # create interface between my class 'ComplexNumber' and types: 'int', 'float'
        if isinstance(other, (float, int)):
            other = ComplexNumber(other)
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __radd__(self, other):
        if isinstance(other, (float, int)):
            other = ComplexNumber(other)
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, (float, int)):
            other = ComplexNumber(other)
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __rsub__(self, other):
        if isinstance(other, (float, int)):
            other = ComplexNumber(other)
        return self.__sub__(other)

    def __mul__(self, other):
        if isinstance(other, (float, int)):
            other = ComplexNumber(other)
        return ComplexNumber(self.real * other.real - self.imag * other.imag,
                             self.imag * other.real + self.real * other.real)

    def __truediv__(self, other):
        if isinstance(other, (float, int)):
            other = ComplexNumber(other)
        divisor = (other.real ** 2 + other.imag ** 2)
        return ComplexNumber((self.real * other.real) - (self.imag * other.imag) / divisor,
                             (self.imag * other.real) + (self.real * other.imag) / divisor)

    def __abs__(self):
        return cmath.sqrt(self.real ** 2 - (self.imag ** 2))

    def __neg__(self):
        return ComplexNumber(-self.real, -self.imag)

    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag

    def __ne__(self, other):
        return not self.__eq__(other)

    def __pos__(self):
        return self

    @staticmethod
    def _illegal(operator):
        print(f"Illegal operation {operator} for complex numbers")

    def __gt__(self, other):
        self._illegal('>')

    def __ge__(self, other):
        self._illegal('>=')

    def __lt__(self, other):
        self._illegal('<')

    def __le__(self):
        self._illegal('<=')


if __name__ == '__main__':
    # example of usage

    num1 = ComplexNumber(1, 2)
    num2 = ComplexNumber(3, 4)
    print(f"Adding numbers {num1} + {num2} = {num1 + num2}")
    print(f"Subtracting numbers {num1} - {num2} = {num1 - num2}")
    print(f"Multiplying numbers {num1} * {num2} = {num1 * num2}")
    print(f"Dividing numbers: {num1} / {num2} = {num1 / num2}")
    print(f"Absolute value of {num1} = {abs(num1)}")
    print(f"Negation of {num1} = {-num1}")

    num3 = 12
    print(f"Adding float to complex number: {num1 + num3}")
