tc = int(input())
while (tc > 0):
    count = 0
    str1 = input()
    str2 = input()
    for k, v in enumerate(str1[:]):
        if (v in str2):
            # print(v)
            str1 = str1.replace(v, "", 1)
            str2 = str2.replace(v, "", 1)
            # print(str1 , str2)

    tc -= 1
    print(len(str1) + len(str2))