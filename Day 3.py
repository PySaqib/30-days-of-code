#!/bin/python3

def check(n):
    if (n%2 != 0):
        print("Weird")
    else:
        if(n >= 2 and n <= 5):
            print("Not Weird")
        elif(n >= 6 and n <= 20):
            print("Weird")
        elif(n > 20):
            print("Not Weird")

if __name__ == '__main__':
    N = int(input())
    check(N)