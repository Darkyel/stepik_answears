/step/3

function testIf(a, b) {
    var x;
    if(a>b){
        x=a+b
    }
    else{
        x=a*b
    }
    return x;
}

/step/5

function testIf(a, b) {
    var x;
    if(a<b){
       x=a+b 
    }
    else if(a>b){
       x=a-b 
    }
    else{
      x=a*b  
    }
    return x;
}

/step/8

testCase = a => {
    switch (a) {     
        case 0: return "Ноль"; 
        case 1: return "Один";  
        case 2: return "Два";  
        case 3: return "Три";  
        case 4: return "Четыре";  
        case 5: return "Пять";  
        case 6: return "Шесть"; 
        case 7: return "Семь"; 
        case 8: return "Восемь";
        case 9: return "Девять";
    }
};
