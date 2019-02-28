#!/bin/python3

phoneDirectory = {}

def addRecord(str):
    phoneNum = int(str[-8:])
    name = str[:-9]

    phoneDirectory[name] = phoneNum

if __name__ == "__main__":
    n = int(input())

    for i in range(0, n):
        query = input()
        addRecord(query)
    
    try:
        while (True):
            query = input()
            if (query != ''):
                record = phoneDirectory.get(query)
                
                if(record != None):
                    print(query + "=" + str(record))
                else:
                    print("Not found")
            else:
                break
    except:
        pass
