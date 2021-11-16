/step/5

function myFunction() { };
var myFunction = function(a) {document.write(a); } ;
function Function(a) { document.write(a); };

/step/9

Функцию можно определить и сразу вызвать в рамках одной команды
Функция, имеющая имя, может вызывать сама себя
Команду return можно вовсе не использовать в функции

/step/10

function my_function(n) {
  if (n == 1) 
    return n.toString();             
  else 
    return my_function(n - 1) + " " + n;
}
