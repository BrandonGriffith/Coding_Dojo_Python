function solution(number){
    number--;
    var num = 0;
    if(number < 1){
        return 0;
    }
    while(number > 0){
        if(number % 3 == 0 || number % 5 == 0){
            num += number;
        }
        number--;
    }
    return num;
}


console.log(solution(10));
