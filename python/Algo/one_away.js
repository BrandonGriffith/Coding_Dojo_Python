function oneAway(str1, str2) {
    var end = 0;
    var runner1 = 0;
    var runner2 = 0;
    if(str1.length > str2.length && str1[0] != str2[0]){
        runner1++;
    }
    while(runner1 < str1.length || runner2 < str2.length) {
        if(str1[runner1] == str2[runner2]) {
            runner1++;
            runner2++;
        }else if(str1[runner1] == str2[runner2+1]) {
            runner1++;
            runner2++;
        }else{
            runner1++;
            runner2++;
            end++;
        }
    }
    runner1 = str1.length-1;
    runner2 = str2.length-1;
    while(runner1 >= 0 || runner2 >= 0) {
        if(str1[runner1] == str2[runner2]) {
            runner1--;
            runner2--;
        }else if(str1[runner1-1] == str2[runner2]) {
            runner1--;
            runner2--;
        }else{
            runner1--;
            runner2--;
            end++;
        }
    }if(end > 2) {
        return false;
    }return true;
}

console.log(oneAway("hello", "eello")) // true
console.log(oneAway("hello", "eelloo")) // false 
console.log(oneAway("ello", "hello")) // true
console.log(oneAway("helllo", "hello")) // true
console.log(oneAway("hello", "helo")) // true
console.log(oneAway("hello", "hell")) // true
console.log(oneAway("hjllo", "helo")) // false
console.log(oneAway("hello", "ello")) // true


