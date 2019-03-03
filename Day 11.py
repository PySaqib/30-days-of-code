#!/bin/python3


A = [[6,6,8,2,4,2],
     [6,6,6,4,2,3],
     [8,6,6,5,8,0],
     [1,4,3,0,4,3],
     [4,9,2,0,8,2],
     [2,7,6,0,9,6]]

def findHourglass(A):
    crRow = 1
    crCol = 0

    hrGlass = []
    hrGlassSum = []

    while(crRow <= len(A) - 1):
        try:
            hrGlass.append(
                [A[crRow - 1][crCol], A[crRow - 1][crCol + 1], A[crRow - 1][crCol + 2],
                A[crRow][crCol + 1],
                A[crRow + 1][crCol], A[crRow + 1][crCol + 1], A[crRow + 1][crCol + 2]])
            crCol += 1
        except:
            crRow += 1
            crCol = 0

    for i in range(0, len(hrGlass)):
        hrGlassSum.append(sum(hrGlass[i]))
    
    print(max(hrGlassSum))

findHourglass(A)