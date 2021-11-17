/step/2

def decode_strings(item):
    s = ''
    result = ''
    i = 0
    tempnum = ''
    length = len(item) - 1
    while i <= (len(item) - 1):
        if item[i].isalpha():
            s = item[i]
            i += 1
        else:
            while item[i].isdigit() and i < (len(item) - 1):
                tempnum = str(tempnum) + str(item[i])
                i += 1
            if i == len(item) - 1:
                tempnum = str(item[i])
                s = s * int(tempnum)
                result = result + s
                return(result)
            s = s * int(tempnum)
            result = result + s
            tempnum = ''

with open('C:\\Users\\igors\\Downloads\\dataset_3363_2.txt', 'r') as dec, open('C:\\Users\\igors\\Downloads\\dataset_3363_2_answer.txt', 'w') as wr:
    for line in dec:
       line = line.strip()
       wr.write(decode_strings(line) + "\n")
      
/step/3

def words_count(wall_of_text):
    counter = 0
    freq = {}
    w = wall_of_text.split()

    for i in w:
        i = i.lower()
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
            
    result = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    print(*result[0])

with open('C:\\Users\\igors\\Downloads\\dataset_3363_3.txt', 'r') as words:
    fulltext = ''
    for line in words:
        line = line.replace('\n', ' ')
        fulltext += line
    words_count(fulltext)
    
/step/4

table =[]

with open('C:\\Users\\igors\\Downloads\\dataset_3363_4.txt', 'r') as abi:
    for line in abi:
        line = line.strip()
        # temp = line.split(';')
        table.append(line)

for i in range(len(table)):
    table[i] = table[i].split(';')

math_sum = 0
phys_sum = 0
rus_sum = 0

with open('C:\\Users\\igors\\Downloads\\dataset_3363_4_answers.txt', 'w') as wr:
    all_av = ''
    for surname in range(len(table)):
        average = list(map(float, table[surname][1:]))
        average = str(round(sum(average) / 3, 9))
        wr.write(average + "\n")
        math_sum += int(table[surname][1])
        phys_sum += int(table[surname][2])
        rus_sum += int(table[surname][3])
    wr.write(str(round((math_sum / len(table)), 9)) + " " + str(round((phys_sum / len(table)), 9)) + " " + str(round((rus_sum / len(table)), 9)))
