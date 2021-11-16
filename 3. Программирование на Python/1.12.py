/step/1

def get_triangle_area_by_geron(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5
print(get_triangle_area_by_geron(int(input()), int(input()), int(input())))

/step/2

def is_in_interval(n):
    return (-15 < n <= 12) or (14 < n < 17) or (19 <= n)
print(is_in_interval(int(input())))

/step/3

def calculate(a, b, op):
    result = 0
    if op == '+':
        result = a + b
    elif op == '-':
        result = a - b
    elif op == '*':
        result = a * b
    elif op == 'pow':
        result = a ** b
    elif op == '/':
        result = a / b
    elif op == 'mod':
        result = a % b
    elif op == 'div':
        result = a // b
    return result
try:
    print(calculate(float(input()), float(input()), input()))
except ZeroDivisionError as e:
    print('Деление на 0!')

/step/4

def get_circle_area(r):
    return 3.14 * (r ** 2)
def get_triangle_area(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5
def get_rectangle_area(a, b):
    return a * b
form = input()
area = 0
if form == 'треугольник':
    area = get_triangle_area(float(input()), float(input()), float(input()))
elif form == 'прямоугольник':
    area = get_rectangle_area(float(input()), float(input()))
elif form == 'круг':
    area = get_circle_area(float(input()))
print(area)

/step/5

def get_max_min_middle(data):
    sorted_data = sorted(data)
    return sorted_data[2], sorted_data[0], sorted_data[1]
for param in get_max_min_middle(int(input()) for _ in range(3)):
    print(param)
    
/step/6

s = int (input())
n1 =" программистов"
n2 =" программист"
n3 =" программиста"
if  s>=0:
  if s==0:
    print(str(s) + n1)
  elif s%100>=10 and s%100<=20:
    print(str(s) + n1)
  elif s%10==1:
    print(str(s) + n2)
  elif s%10>=2 and s%10<=4:
    print(str(s) + n3)
  else:
    print(str(s) + n1)
    
/step/7

def is_lucky(ticket_number):
    even = sum([int(ticket_number[i]) for i in range(len(ticket_number) // 2)])
    odd = sum([int(ticket_number[i]) for i in range(len(ticket_number) // 2, len(ticket_number))])
    return even == odd
def get_ticket_status(ticket_number):
    return 'Счастливый' if is_lucky(ticket_number) else 'Обычный'
print(get_ticket_status(input()))
