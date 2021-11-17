/step/1

table = []
teams = {}
points = 0
match_count = 0
victories = 0
draws = 0
losses = 0
i = 0
n = int(input())
while i <= n - 1:
    match = str(input())
    table.append(match)
    i += 1
for i in range(len(table)):
    table[i] = table[i].split(';')
    teams[table[i][0]] = [match_count, victories, draws, losses, points]
    teams[table[i][2]] = [match_count, victories, draws, losses, points]
for i in range(len(table)):
    # [['Зенит', 3, 'Спартак', 1]]
    table[i][1] = int(table[i][1])
    table[i][3] = int(table[i][3])
    if table[i][1] > table[i][3]:
        teams[table[i][0]][0] += 1
        teams[table[i][0]][1] += 1
        teams[table[i][0]][4] += 3
        teams[table[i][2]][0] += 1
        teams[table[i][2]][3] += 1
    elif table[i][1] < table[i][3]:
        teams[table[i][2]][0] += 1
        teams[table[i][2]][1] += 1
        teams[table[i][2]][4] += 3
        teams[table[i][0]][0] += 1
        teams[table[i][0]][3] += 1
    else:
        teams[table[i][2]][0] += 1
        teams[table[i][2]][2] += 1
        teams[table[i][2]][4] += 1
        teams[table[i][0]][0] += 1
        teams[table[i][0]][2] += 1
        teams[table[i][0]][4] += 1
for fclub, stat in teams.items():
    str_stat = list(map(str, stat))
    print(fclub + ':' + ' '.join(str_stat))
    
/step/2

def ende_code(s, encode, a_from, a_to):
    code = dict()
    if encode:
        tmp = a_from
        a_from = a_to
        a_to = tmp
    for i in range(len(a_from)):
        code[a_from[i]] = a_to[i]
    result = ''
    for c in s:
        result += code[c]
    return result
or_alf = input()
co_alf = input()
or_str = input()
co_str = input()
print(ende_code(or_str, False, or_alf, co_alf))
print(ende_code(co_str, True, or_alf, co_alf))

/step/3

n = int(input())
known_words = []
checked_words = []
errors = {}
for i in range(n):
    vocab = str(input()).lower()
    known_words.append(vocab)
k = int(input())
for j in range(k):
    checked = input().split()
    checked_words.append(checked)
checked_words = [w.lower() for line in checked_words for w in line]
for j in checked_words:
    if j not in known_words:
        errors[j] = 'Unknown word'
for error in errors.keys():
    print(error)
    
/step/4

x = 0
y = 0
n = int(input())
for i in range(n):
    napr, cnt = input().lower().split()
    cnt = int(cnt)
    if napr == 'север':
        y += cnt
    elif napr == 'юг':
        y -= cnt
    elif napr == 'восток':
        x += cnt
    elif napr == 'запад':
        x -= cnt
print(x, end=' ')
print(y)

/step/5

table = []
res = {}
counter = {}
with open('C:\\Users\\igors\\Downloads\\dataset_3380_5.txt', 'r') as school:
    for line in school:
        line = line.strip()
        table.append(line)
for i in range(len(table)):
    table[i] = table[i].split()
for j in range(len(table)):
    table[j][2] = int(table[j][2])
    if table[j][0] in res:
        res[table[j][0]] += table[j][2]
        counter[table[j][0]] += 1
    else:
        res[table[j][0]] = table[j][2]
        counter[table[j][0]] = 1
for i in range(1, 12):
    if str(i) in res:
        print('%s %s' % (i, res[str(i)] / counter[str(i)]))
    else:
        print('%s %s' % (i, "-"))
