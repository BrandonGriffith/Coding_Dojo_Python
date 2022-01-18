function ConvertToCoinChange(input) {
    var coins = [0, 0, 0, 0];
    var x = ["counting pennys:   "];

    for ( input; input >= .25; input -= .25 ) {
        coins[0] = coins[0] + 1;
        input = input.toFixed(2);
    }

    for ( input; input >= .10; input -= .10 ) {
        coins[1] = coins[1] + 1;
        input = input.toFixed(2);
    }

    for ( input; input >= .05; input -= .05 ) {
        coins[2] = coins[2] + 1 ;
        input = input.toFixed(2);
    }

    for ( input; input > .00; input -= .01 ) {
        coins[3] = coins[3] + 1;
        input = input.toFixed(2);
        x = x + "            " + input;
    }

    var str = "";

    if ( coins[0] >= 1 ) {
        str = str + coins[0] + " quarters, ";
    }
    if ( coins[1] >= 1 ) {
        str = str + coins[1] + " dimes, ";
    }
    if ( coins[2] >= 1 ) {
        str = str + coins[2] + " nickels, ";
    }
    if ( coins[3] >= 1 ) {
        str = str + coins[3] + " pennys";
    }
    console.log(x)
    return str;
}

console.log(ConvertToCoinChange(3.22));

console.log(ConvertToCoinChange(3.21));

console.log(ConvertToCoinChange(9.68));

console.log(ConvertToCoinChange(0.03));

console.log(ConvertToCoinChange(0.02));

console.log(ConvertToCoinChange(0.01));

console.log(ConvertToCoinChange(1.22));
