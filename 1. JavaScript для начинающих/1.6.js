/step/5

function testFactorial(a) {
    var x = 1; 
    for(i = 1;i <= a;i++){
        x *= i;
        }
    return x;
}

/step/8

function testWhile(a) {
    var x=0;
    var i=1
    while(i<=a){
        if(i%2==0){
            x+=i
            }
        i++
        }
    return x;
}
