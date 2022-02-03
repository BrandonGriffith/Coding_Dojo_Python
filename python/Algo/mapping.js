function mappingItineraries(arr) {
    var one =  []
    var two = []
    var result = []
    for(var i = 0 ; i < arr.length ; i ++ ) {
        one.push(arr[i][0]);
        two.push(arr[i][1]);
    }
    var runner1 = 0;
    var runner2 = 0;
    while(runner2 <= two.length) {
        if(one[runner1] == two[runner2]) {
            runner1++;
            runner2 = 0;
        }else if(runner2 == two.length) {
            result.push(one[runner1]);
            runner2 ++;
        }else {
            runner2 ++;
        }
    }
    var j = 0;
    while(result.length <= two.length) {
        if(result[result.length-1] == arr[j][0]) {
            result.push(arr[j][1]);
            j = 0;
        }else {
            j++
        }
    }
    return result.join(" -> ");
}


console.log(mappingItineraries( [  ['ICN', 'LAX'], ['LAX', 'SFO'], ['SJC', 'ICN'], ['NYU', 'SJC'], ['AMS', 'NYU'] ]));
// AMS -> NYU -> SJC -> ICN -> LAX -> SFO

