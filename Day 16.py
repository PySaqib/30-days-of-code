#!/bin/python3

import sys


S = input().strip()

def strToInt(str):
    try:
        print(int(str))
    except:
        print("Bad String")

strToInt(S)
