/step/4

x=y         <=>   x = 3; y = 3;
x = x + y   <=>   x = 9; y = 3;
x = y - x   <=>   x = -3; y = 3;
x = x * y   <=>   x = 18; y = 3;
x = x % y   <=>   x = 0; y = 3;
x = x / y   <=>   x = 2; y = 3;
x = ++y     <=>   x = 4; y = 4;
x = y++     <=>   x = 3; y = 4;
x = - -y    <=>   x = 2; y = 2;
x = y- -    <=>   x = 3; y = 2;

/step/6

x += y  <=> x = 9
x -= y  <=> x = 3
x *= y  <=> x = 18
x /= y  <=> x = 2
x %= y  <=> x = 0

/step/7

function testSum(a, b) {
   var x;
   x = a + b
   return x;
}

/step/9

Результатом x > 8 будет false
Результатом x != 8 будет true
Результатом x == 8 будет false
Результатом x >= 7 будет true

/step/12

При x = 3 и y = 6 результатом операции !(x > y) будет true
При x = 3 и y = 6 результатом операции x < 3 && y == 6 будет false
При x = 3 и y = 6 результатом операции x == 3 || y > 6 будет true

/step/13

function testOperation(a, b) {
    var x;
    x=2*((a*b)%(a+b))
    return x;
}
