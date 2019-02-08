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
        together as if it were to simulate the distributive property.

        Coefficient representation is as follows:

        c*x^0 + c*x^1 + c*x^2 + ... + c*x^n

        """

        # Index's to help us interact through double nested for loop.
        outerLoopIndex = 0
        innerLoopIndex = 0

        # Special exception for when first run through for OuterLoopIndex = 0
        needToPopFirstZero = True

        # Polynomials to hold our values between for loop iterations
        tempPolynomial = Polynomial([])
        bigPolynomial = Polynomial([])

        # After each iteration of this loop, it will add 2 coefficient segments together
        for x in range(len(self)):

            # Each loop of this will times two integers together, and then add them to a temp
            # polynomial.
            for y in range(len(rhs)):

                # Take one coefficient from the left side, and times it against one on the right side.
                tempPolynomial.coefficients = tempPolynomial.coefficients + ([self.coefficients[outerLoopIndex] * rhs.coefficients[innerLoopIndex]])

                # Special exception for the first run through, getting ride of zero.
                if needToPopFirstZero:

                    # Pop the first zero because we don't want it yet. First
                    # time through doesn't need a zero to offset the polynomial
                    tempPolynomial.coefficients = [tempPolynomial.coefficients.pop()]
                    needToPopFirstZero = False

                # Iterate the value for the next loop.
                innerLoopIndex = innerLoopIndex + 1

            # Save the end result here after each loop by adding two polynomials
            # together.
            bigPolynomial.coefficients = (bigPolynomial + tempPolynomial).coefficients

            # Call recursive function to pad the from of the polynomial as many
            # times as we need to, to create a viable adding between two
            # coefficients
            tempPolynomial.coefficients = addZero(outerLoopIndex)

            # Increase outerloop index, and reset inner loop.
            outerLoopIndex = outerLoopIndex + 1
            innerLoopIndex = 0

        # return the final option.
        return Polynomial(bigPolynomial.coefficients)

    def __len__(self):

        """

        This will return the length of the polynomial.
        """

        return len(self.coefficients)


# Recursive function to add padding to the front of a polynomial
# to help with the addition process. Only for Mult function.
def addZero(numOfIterations):

    if numOfIterations+1 == 1:
        return [0]
    elif numOfIterations+1 > 1:
        return [0] + addZero(numOfIterations - 1)


# Test cases for len function
def test_len():

    p1 = Polynomial([2])
    p2 = Polynomial([3, 2])

    assert len(p1) == 1
    assert len(p2) == 2


# Test cases for the call function. If we evaluate xm
# with a simple cx^0 + cx^1 + cx^2 + ... + cx^n notation
def test_call():

    p1 = Polynomial([2])
    p2 = Polynomial([3, 2])
    p7 = Polynomial([1, 5, 8, 2, 34])

    assert p1(x=5) == 2
    assert p2(x=5) == 13
    assert p7(x=4) == 8981


# Test cases for mult function
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


# Test cases for add function
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


# A main function that doesn't really serve a purpose
if __name__ == '__main__':
    p = Polynomial([1, 5, 6])
    p2 = p + p
    p3 = p * p2
    value = p3(45.8)
