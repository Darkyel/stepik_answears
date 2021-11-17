/step/3

10555

/step/8

def f(x):
    result = 0
    if x <= -2:
        result = 1 - (x + 2)**2
    elif -2 < x <= 2:
        result = -(x / 2)
    elif 2 < x:
        result = (x - 2)**2 + 1
    return result
  
/step/9

def modify_list(l):
    l[:] = [i // 2 for i in l if not i % 2]
