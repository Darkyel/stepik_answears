/step/5

function testArray(a, b) {
    var c = a.concat(b);
    var s =0;
    for (i=0 ;i < c.length;i++)
    {
       s+=c[i];
    }
    return s;
}

/step/9

Метод pop() удаляет из массива один элемент - последний
Единственный метод, позволяющий добавлять элементы в середину массива - это метод splice()

/step/10

function testArray(a, b) {
    var c = a.concat(b)
    var s = c.split('')
    var m = s.reverse()
    var n = m.join('')
    var b = n + "Иванов"
    return b
}
