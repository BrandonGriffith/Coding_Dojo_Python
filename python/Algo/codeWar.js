function even_or_odd(number) {
    var x = "";
    if (number % 2 == 0){
        x = "Even";
    }else{
        x = "Odd";
    }
    return x;
}
console.log(even_or_odd(9));
console.log(even_or_odd(2));
console.log(even_or_odd(1));
console.log(even_or_odd(18));
console.log(even_or_odd(5));