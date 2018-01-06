# number of deletions to make string anagrams ..
import numpy as np
n = int(input())
count= 0
#print (n)
for i in range(0,n):
    #print (i)
    a = list(input())
    b = list(input())
    al = len(a)
    bl = len(b)
    #print(a)
    for x in range(0,al) :
       # print("x "+x)
       # print("b " + b)

        for y in range (0,bl):

            #print("b " + y)

            if (a[x]==b[y]):
               # print("y "+ y)
                b[y] = 0
                count+=1
                #print(count)
                break
    print(al+bl-count*2)
    count = 0

