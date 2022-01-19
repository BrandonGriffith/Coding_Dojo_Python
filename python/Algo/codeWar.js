function squareDigits(num){
    var x = "";
    num = num.toString();
    num = num.split('');
    for(i=0;i<num.length;i++){
        var z = parseInt(num[i]) ** 2;
        x += z.toString();
    }
    x = parseInt(x);
    return x;
}

console.log(squareDigits(211));
