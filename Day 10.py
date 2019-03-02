#!/bin/python3

import math
import os
import random
import re
import sys

# Doing it the traditional way
def decToBin(n):
    bin = ''
    while (n >= 1):
        bin += str(n%2)
        n = int(n/2)
    bin += str(n)
    return consecFind(bin[::-1])

# Function to find consecutive ones

def consecFind(str):
    counter = 0
    log = []
    for i in range(0, len(str)):
        if (str[i] == '1'):
            counter += 1

            if (i + 1) < len(str):
                if (str[i + 1] == '1'):
                    continue
                else:
                    log.append(counter)
                    counter = 0
            else:
                log.append(counter)
                counter = 0

        else:
            continue
    
    return(max(log))
        


if __name__ == '__main__':
    n = int(input())
    print(decToBin(n))