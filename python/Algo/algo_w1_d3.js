function isPallindrome(str){
    for (i = 0; i < str.length/2; i++){
        x = str.length - 1
        if (str[i] !== str[x - i]){
            return false;
        }
    }
    return true;
}

console.log(isPallindrome("racecar")); //true
console.log(isPallindrome("e tacocat e")); //true
console.log(isPallindrome("Dud")); //false
console.log(isPallindrome("oho!")); //false
console.log(isPallindrome(" to ")); //false

console.log("-------------------------------------------------");


longPall = "";
function longestPallindrome(str){
    notPall = "this is not a pallindrome.";
    pall1 = "";
    pall2 = "";
    j = 0;
    isPall = " is the new longest pallindrome.";
    for (i = 0; i < str.length/2; i++){
        x = str.length - 1
        if (str[i] === str[x-i]){
            pall1 = pall1 + str[i];
            pall3 = pall2;
            pall2 = str[x-i] + pall3;
            if (pall1.length + pall2.length > longPall.length){
                longPall = pall1 + pall2;
                j++;
            }
        }
    }
    if (j != 0){
        longPall = longPall;
        return longPall + isPall;
    }
    else{
        return notPall;
    }
}

console.log(longestPallindrome("my favorite racecar erupted"));
console.log(longestPallindrome("nada"));
console.log(longestPallindrome("nothing to see"));
console.log(longestPallindrome("racecar"));
console.log(longestPallindrome("e tacocat e"));
console.log(longestPallindrome("Dud"));
console.log(longestPallindrome("oho!"));
console.log(longestPallindrome(" to "));


function longestPallindrome(str) {
    var palli = "";
    
    for (var i = 0 ; i < str.length-1 ; i ++) {
        for (var j = i + 1; j <= str.length ; j ++) {
            // check to see if this section of the string is a pallindrome
            if (isPallindrome(str.slice(i,j)) === true) {
                // is this new pallindrome's length greater than the existing 'longest pallindrome'?
                if (str.slice(i,j).length > palli.length) {
                    palli = str.slice(i,j);
                }
            }
        }
    }
    return palli;
}

console.log(longestPallindrome("my favorite racecar erupted"));
console.log(longestPallindrome("nada"));
console.log(longestPallindrome("nothing to see"));