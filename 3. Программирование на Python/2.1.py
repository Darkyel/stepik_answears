/step/4

13

/step/5

9

/step/9

17

/step/11

numbers = []
while True:
    x = int(input())
    numbers.append(x)
    if x == 0:
        break
print(sum(numbers))


/step/12

def lcm(a, b):
    c = a * b
    result = c
    while c > 0:
        if c % a == 0 and c % b == 0:
            result = c
        c -= 1
    return result
print(lcm(int(input()), int(input())))
