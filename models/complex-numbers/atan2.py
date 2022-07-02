"""
During the creation of complexNumbers.py I came across a function atan2.
I wrote it myself, let's see how it compares with atan2 builtins
"""
from complexNumbers import Complex
import math
import random
import time


class FunctionTest(object):
    """
    A class to compare speed of math.atan2 to Complex.complexArgument of mine
    """

    def __init__(self, number_of_tests=10**6, min_re=-1 * 10 ** 100, max_re=10 ** 100, min_im=-1 * 10 ** 100, max_im=10 ** 100):
        self.tests = [[random.randint(min_re, max_re), random.randint(min_im, max_im)] for k in range(number_of_tests)]
        self.cumulative_builtin = 0
        self.cumulative_mine = 0
        for test in self.tests:
            print(f"For the given Re={test[0]} Im={test[1]}")
            print(f"---")

            # math.atan2
            start_time = time.time()
            atan_val = math.atan2(test[1], test[0])
            atan_diff = time.time() - start_time
            print(f"{atan_diff}|{atan_val}|math.atan2")

            # Complex.complexArgument
            start_time = time.time()
            my_val = Complex.complexArgument(test[0], test[1])
            my_diff = time.time() - start_time
            print(f"{my_diff}|{my_val}|Complex.complexArgument")

            self.cumulative_builtin += atan_diff
            self.cumulative_mine += my_diff
        print(f"Over the course of {number_of_tests} tests:")
        if self.cumulative_mine > self.cumulative_builtin:
            print(f"math.atan2 has won with the difference of "
                  f"{self.cumulative_mine - self.cumulative_builtin} seconds")
        else:
            print(f"Complex.complexArgument has won with the difference of "
                  f"{self.cumulative_builtin - self.cumulative_mine} seconds")


FunctionTest()
