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

        tempList = []

        index = 0;

        if len(rhs) > len(self):
            self.coefficients = self.pad(self.coefficients, len(rhs))
        elif len(rhs) < len(self):
            rhs.coefficients = rhs.pad(rhs.coefficients, len(self))

        for x in range(len(rhs)):
            tempList = tempList + ([self.coefficients[index] + rhs.coefficients[index]])
            index = index + 1

        return Polynomial(tempList)

    def __mul__(self, rhs):

        outerLoopIndex = 0
        innerLoopIndex = 0

        tempList = []

        for x in range(len(self)):
            for y in range(len(rhs)):
                tempList = tempList + ([self.coefficients[outerLoopIndex] * rhs.coefficients[innerLoopIndex]])



        return Polynomial(tempList)

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


def test_mult():

    p1 = Polynomial([2])
    p2 = Polynomial([3])
    p3 = Polynomial([5])
    p4 = Polynomial([10])
    p5 = Polynomial([1, 2])
    p6 = Polynomial([5, 7])
    p7 = Polynomial([1, 5, 8, 2, 34])

    assert (p1 * p2).coefficients == [6]
    assert (p2 * p4).coefficients == [30]

    assert (p1 * p5).coefficients == [2, 4]

def test_add0():

    p1 = Polynomial([2])
    p2 = Polynomial([3])
    p3 = Polynomial([5])
    p4 = Polynomial([10])
    p5 = Polynomial([1,2])
    p6 = Polynomial([5,7])
    p7 = Polynomial([1,5,8,2,34])

    # Tests of lists of length one
    assert (p1 + p2).coefficients == [5]
    assert (p1 + p2 + p3).coefficients == [10]
    assert (p1 + p2 + p3 + p4).coefficients == [20]

    # Tests of lists of length two
    assert (p5 + p6).coefficients == [6, 9]
    assert (p5 + p6).coefficients == [6, 9]

    # Test with differing length
    assert (p1 + p5).coefficients == [3, 2]

    # Tests with lists of different length, as well as one list
    # being bigger than the other, then inverted.
    assert (p2 + p6 + p7).coefficients == [9, 12, 8, 2, 34]
    assert (p7 + p2 + p6).coefficients == [9, 12, 8, 2, 34]
    assert (p6 + p7 + p2).coefficients == [9, 12, 8, 2, 34]



if __name__ == '__main__':
    p = Polynomial([1, 5, 6])
    p2 = p + p
    p3 = p * p2
    value = p3(45.8)
