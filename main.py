# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 10:43:18 2019

@author: spencer.stewart
"""


class Polynomial:
    """

    Represents a polynomial in x based coefficients.
    With the smallest power leading.

    """

    def __init__(self, cs):
        """
        initialize polynomial with coefficients: cs
        cs is a list
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

        """
        This will take two polynomial coefficients and add them together
        and then return them.

        This works if you are trying to add multiple polynomials together
        in one line
        """

        # This will hold the new coefficient list we want to send back
        tempList = []

        # This helps us iterate our for loop.
        index = 0

        # If one polynomials is longer than the other, this will equalize them with paddings of zeros
        # on the end of the shorter polynomial
        if len(rhs) > len(self):
            self.coefficients = self.pad(self.coefficients, len(rhs))
        elif len(rhs) < len(self):
            rhs.coefficients = rhs.pad(rhs.coefficients, len(self))

        # For loop to add each of the coefficients together.
        for x in range(len(rhs)):
            tempList = tempList + ([self.coefficients[index] + rhs.coefficients[index]])
            index = index + 1

        # Return a polynomial with new coefficients
        return Polynomial(tempList)

    def __mul__(self, rhs):

        """

        This function will take two polynomial coefficients and then multiply them
        together as if it were to simulate a

        """
        outerLoopIndex = 0
        innerLoopIndex = 0

        isNotPopped = True

        tempPolynomial = Polynomial([])
        bigPolynomial = Polynomial([])

        for x in range(len(self)):
            for y in range(len(rhs)):

                print("OuterLoop Index: ", outerLoopIndex)
                print("InnerLoop Index: ", innerLoopIndex)

                print("self coeff", self.coefficients)
                print("rhs coeff", rhs.coefficients)

                print("AddZero function is: ", addZero(outerLoopIndex))
                print("tempPolynomial.coefficients: ", tempPolynomial.coefficients)
                print("AddZero and tempPoly coeff: ", (addZero(outerLoopIndex) + tempPolynomial.coefficients))
                print("self:", self.coefficients[outerLoopIndex])
                print("rhs:", rhs.coefficients[innerLoopIndex])

                print("self * rhs:", [self.coefficients[outerLoopIndex] * rhs.coefficients[innerLoopIndex]])

                tempPolynomial.coefficients = tempPolynomial.coefficients + ([self.coefficients[outerLoopIndex] * rhs.coefficients[innerLoopIndex]])

                print("tempPolynomial.coefficients: ", tempPolynomial.coefficients)

                if isNotPopped:
                    tempPolynomial.coefficients = [tempPolynomial.coefficients.pop()]
                    isNotPopped = False

                    print("if statement was called")

                print("tempPolynomial.coefficients: ", tempPolynomial.coefficients)


                print("")
                print("")
                print("")
                print("")
                innerLoopIndex = innerLoopIndex + 1

            bigPolynomial.coefficients = (bigPolynomial + tempPolynomial).coefficients
            print("This is big list: ", bigPolynomial.coefficients)

            tempPolynomial.coefficients = addZero(outerLoopIndex)
            outerLoopIndex = outerLoopIndex + 1
            innerLoopIndex = 0


        print("This is big list end: ")
        print(bigPolynomial.coefficients)
        print(tempPolynomial.coefficients)


        print(bigPolynomial.coefficients)

        return Polynomial(bigPolynomial.coefficients)

    def __len__(self):

        return len(self.coefficients)

def addZero(numOfIterations):

    if numOfIterations+1 == 1:
        return [0]
    elif numOfIterations+1 > 1:
        return [0] + addZero(numOfIterations - 1)

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

    assert (p5 * p6).coefficients == [5, 17, 14]
    assert (p1 * p5).coefficients == [2, 4]

    assert (p1 * p2 * p3).coefficients == [30]
    assert (p1 * p6 * p7).coefficients == [10, 64, 150, 132, 368, 476]

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
