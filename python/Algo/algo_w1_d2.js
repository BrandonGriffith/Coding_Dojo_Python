function parensValid(str){
    var x = 0;
    var y = 0;
    for(var i = 0; i < str.length; i ++){   
        if(str[i] == "("){
            x++;
            y++;
        }
        else if(str[i] == ")"){
            x--;
            if(y == 0){
                return false;
            }
        }
        }
    if (x != 0){
        return false;
    }
    return true;
}

console.log(parensValid("y(3(p)p(3)r)s")); // true
console.log(parensValid("n(0(p)3")); // false
console.log(parensValid("n)0(t(o)k")); // false
console.log(parensValid("((()))")); // true
console.log(parensValid("()()()()()()(")); // false

console.log("----------------------------------------------------")

function bracesValid(str){
    var x = 0;
    var y = 0;
    var x2 = 0;
    var y2 = 0;
    for(var i=0; i < str.length; i++){
        if(str[i] == '('){
            y++;
            y2++;
        } 
        else if(str[i] == ')'){
            y--;
            if(y2 == 0){
                return false;
            }
        }
        if(str[i] == '{'){
            x++;
            x2++;
        } 
        else if(str[i] == '}'){
            x--;
            if(x2 == 0){
                return false;
            }
        }
    }
    if(x != 0){
        return false
    }
    else if(y != 0){
        return false
    }
    return true
}

console.log(bracesValid("({[({})]})")); // true 
console.log(bracesValid("d(i{a}l[t]o)n{e!")); // false
console.log(bracesValid("{{[a]}}(){bcd}{()}")); // true
