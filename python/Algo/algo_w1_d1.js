// #1) Implement reverseString(str) that takes in a String, and then returns a string of the same length, but with the characters reversed.

// Example: "creature" ---> "erutaerc"

// ** Don't use the built-in reverse() method!

function reverseString(str) {
    // your code here
    var newstr = ""
    for(var i = str.length-1; i >= 0; i--){
        newstr += str[i]
    }
    return newstr
}

console.log(reverseString("creature")); // "erutaerc"

// #2) Create a function that, given a string, returns the string's acronym (first letter's only, capitalized).

// Example: "there's no free lunch - gotta pay yer way" --> "TNFL-GPYW""

function acronym(str) {
    // your code here
    var acro = "";
    for(i = 0; i < str.length; i++){
        if (i == 0){
            acro += str[i].toUpperCase();
        }else if (str[i] == " "){
            acro += str[i+1].toUpperCase();
        }
    }
    return acro;
}

console.log(acronym("there's no free lunch - gotta pay yer way"));
