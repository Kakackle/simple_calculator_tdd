# -*- coding: utf-8 -*-

import operator
import math
from functools import reduce
from functools import reduce


class SimpleCalculator:
    def add(self, *args):
        return sum(args)
    
    def sub(self, a, b):
        return a - b
    
    def mul(self, *args):
        #check for 0s in args
        if not all(args):
            raise ValueError

        def mul2(a,b):
            return a*b
        return reduce(mul2, args)

    def div(self, a, b):
        if not b:
            return float('inf')
        return a / b
    
    def average(self, *args, ut=float('inf'), lt=-1*float('inf')):
        args = [arg for arg in args if arg < ut]
        args = [arg for arg in args if arg > lt]

        if not args:
            return 0

        arg_sum = sum(args)
        return float(arg_sum / len(args))

    # def div(self, a, b):
    #     try:
    #         return a / b
    #     except ZeroDivisionError:
    #         return float("inf")

    # def avg(self, it, lt=None, ut=None):
    #     count = 0
    #     total = 0

    #     for number in it:
    #         if lt is not None and number < lt:
    #             continue
    #         if ut is not None and number > ut:
    #             continue
    #         count += 1
    #         total += number

    #     if count == 0:
    #         return 0

    #     return total / count
