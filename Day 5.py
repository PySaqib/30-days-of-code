#!/bin/python3

import math
import os
import random
import re
import sys

def createTable(n):
    for i in range(1, 11):
        print("{n} x {i} = {ans}".format(n=n, i=i, ans=n*i))

if __name__ == '__main__':
    n = int(input())
    createTable(n)
