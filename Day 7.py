#!/bin/python3

import math
import os
import random
import re
import sys

def arrRev(arr):
    revArr = arr[::-1]
    for i in range(0, len(revArr)):
        print(revArr[i], end=' ')
    

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    arrRev(arr)