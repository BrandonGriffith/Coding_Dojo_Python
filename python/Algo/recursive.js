function sigma(num) {
    num = Math.floor(num);
    var sum = 0
    for (i = 0 ; i <= num ; i ++) {
        sum += i
    }
    return sum
}

function recursiveSigma(num) {
    num = Math.floor(num);
    if (num <= 1) {
        return 1
    }
    return num + recursiveSigma(num - 1)
}

function recursiveFactorial(num) {
    num = Math.floor(num);
    if(num <= 1) {
        return 1;
    }
    return num * recursiveFactorial(num - 1);
}

function recursiveFibonacci2(num) {
    if (num <= 0) {
        return 0;
    } else if (num <= 1) {
        return 1;
    }
    return recursiveFibonacci(num - 2) + recursiveFibonacci(num - 1);
}

function recursiveFibonacci(num) {
    while(num < 2){
        return num;
    }
    return recursiveFibonacci(num - 2) + recursiveFibonacci(num - 1);
}

function recursiveGreatestCommonFactor(num1,num2) {
    if(num1 % num2 != 0){
        console.log(num2);
        return recursiveGreatestCommonFactor(num2, num1 % num2);
    }
    return num2;
}



console.log(recursiveSigma(9));
console.log(recursiveFactorial(9));
console.log(recursiveFibonacci(9));
console.log('____________________________________________');
console.log(recursiveGreatestCommonFactor(9,12));
