/step/5

def update_dictionary(d, key, value):
    if key in d:
        d[key] += [value]
    else:
        d.setdefault(2 * key, []).append(value)
        
/step/6

from collections import Counter
cnt = Counter(input().lower().split())
for key in cnt:
    print(key, cnt[key])
    
/step/7

result = {}
for i in range(int(input())):
    x = int(input())
    if x not in result.keys():
        result[x] = f(x)
    print(result[x])
