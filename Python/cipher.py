'''Hacker earth cypher practice'''
name = input()
number = int(input())

l  = len(name)
for i in range (0, l):
    if ((ord(name[i])>=65 and ord(name[i])<= 90)or (ord(name[i])>=97 and ord(name[i])<=122)):
            y = chr(ord(name[i]) + number %26 )
            x = ord(y)
            if x > 122:
                x = x - 122 + 96
            elif (x > 90 and x < 122 and ord(name[i]) <= 90):
                x = x - 90 + 64
            elif (x > 57 and x < 65 and ord(name[i]) <= 65):
                x = x - 57 + 47
            y = chr(x)
            print(y, end='', flush=True)
    elif (ord(name[i])>=48 and ord(name[i])<=57) :
           # print(number%9)
            y = chr(ord(name[i]) + number % 10)
            x = ord(y)
            if x > 57:
                x = x -57 + 47
            y = chr(x)
            print(y, end='', flush=True)
    else:
        print(name[i],end='', flush=True)