/step/3

8

/step/7

1 2 3; 1 10 3; 20 10 3; 20 10 3

/step/9

print(sum([int(i) for i in input().split()]))

/step/10

a = [int(i) for i in input().split()]
i = 0
res = []
last = 0
if (len(a) == 1):
    print(*a)
elif (len(a) == 2):
    res = [a[1] * 2, a[0] * 2]
    print(*res)
else:
    while i <= len(a) - 1:
        if i == 0:
            res.append(a[i + 1] + a[-1])
            i += 1
            continue
        if i == len(a) - 1:
            last = a[0] + a[i - 1]
            break
        res.append(a[i + 1] + a[i - 1])
        i += 1
    print(*res, last)
    
/step/11

a = [int(i) for i in input().split()]
already = False
res = []
i = 0
a.sort()
if len(a) == 1:
    print()
else:
    while i <= len(a) - 1:
        if i == len(a) - 1:
            if a[-1] == a[-2] and already == False:
                break
            else:
                if already == True:
                    res.append(a[i])
                break
        if a[i] == a[i + 1]:
            i += 1
            already = True
            continue
        else:
            if already == True:
                res.append(a[i])
                already = False
            i += 1
    print(*res)
