/step/4

function testMath(a) {
    b = a * Math.PI / 180
    return Math.sin(b)
}

/step/5

function testMath(a, b, c) {
    var d = c * Math.PI / 180
    var s = 1/2*a*b*Math.sin(d)
    return s
}

/step/7

function testMath(a, b, c, d) {
    var f = Math.min(a,b,c,d)
    var v = Math.max(a,b,c,d)
    var z = Math.floor(v/f)
    return z
}

/step/9

function testMath(a, b) {
    return Math.pow(a,b)
}
