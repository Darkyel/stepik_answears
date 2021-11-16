/step/5

Если в методы replace и search передать вместо регулярного выражения строку, то она будет преобразована в регулярное выражение
Метод replace(regex, str) поддерживает глобальный поиск
Результатом работы метода split() является массив

/step/10

Объект RegExp имеет пять свойств
Конструктор объекта RegExp может принимать на вход либо один либо два аргумента

/step/11

function testRegExp(s, sub_s) {
  var myreg = new RegExp(sub_s,"g");
  var result = s.match(myreg);
  var rr = result.join(",")
  return rr
}
