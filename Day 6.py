def indicePrint(str):
    even = ''
    odd = ''

    for i in range(0, len(str)):
        if (i%2 == 0):
            even += str[i]
        else:
            odd += str[i]
    
    print(even, odd)

if __name__ == '__main__':
    n = int(input())
    
    for i in range(0, n):
        data = input()
        indicePrint(data)
