# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 10:43:18 2019

@author: spencer.stewart
"""


class Polynomial:
    """

    Represents a polynomial in x based coefficients

    """

    def __init__(self, cs):
        """
        initialize polynomial with coefficients: cs
        """
        self.coefficients = cs

    @staticmethod
    def pad(a, m=0):
        """
        returns a new list with the elements of 'a' padded out to size m
        with 0s
        """
        return list(a) + [0] * (m - len(a))

    def __call__(self, x):
        """
        returns p(x) where p is this polynomial
        """
        return sum(ci * x ** i for i, ci in enumerate(self.coefficients))

    def __add__(self, rhs):

        # lCoEff
        # rCoEff

        index = 0;

        if len(rhs) > len(self):
            self.coefficients = self.pad(self.coefficients, len(rhs))

        for x in rhs:
            pass

        return Polynomial([self.coefficients[0] + rhs.coefficients[0]])

    def __mul__(self, rhs):

        return Polynomial([])

    def __len__(self):

        return len(self.coefficients)


def test_len():
    p1 = Polynomial([2])
    p2 = Polynomial([3, 2])

    assert len(p1) == 1
    assert len(p2) == 2


def test_call():
    p1 = Polynomial([2])

    p2 = Polynomial([3, 2])

    assert p1(x=5) == 2
    assert p2(x=5) == 13


def test_add0():
    p1 = Polynomial([2])

    print("We are printing this: ")
    print(p1.coefficients)
    print("End print")

    p2 = Polynomial([3])

    assert p1.__add__(p2).coefficients == [5]

    assert (p1 + p2).coefficients == [5]

    assert (p1 + p2 + p3).coefficients == [5]


if __name__ == '__main__':
    p = Polynomial([1, 5, 6])
    p2 = p + p
    p3 = p * p2
    value = p3(45.8)

"""



"""