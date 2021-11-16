/step/7

Объекты типа Date можно сравнивать между собой
Метод getDay() возвращает день недели даты
После объявления переменной var myDate = new Date(); в переменной окажется текущая дата и время

/step/8

function testDateTime(a, b) {
    var date1 = new Date()
    var date2 = new Date()
    date1.setTime(Date.parse(a))
    date2.setTime(Date.parse(b))
    var days = ["Воскресенье","Понедельник","Вторник","Среда","Четверг","Пятница","Суббота"]
    if (date1 > date2)
    {
        return days[date1.getDay()]
    }
    else
    {
        return days[date2.getDay()]
    }
}
