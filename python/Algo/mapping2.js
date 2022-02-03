function mappingItineraries(arr) {
    var result = []
    var runner1 = 0;
    var runner2 = 0;
    while(runner2 < arr.length) {
        if(arr[runner1][0] == arr[runner2][1]) {
            runner1++;
            runner2 = 0;
        }else if(runner2 == arr.length-1) {
            result.push(arr[runner1][0]);
            runner2 ++;
        }else {
            runner2 ++;
        }
    }
    var j = 0;
    while(result.length <= arr.length) {
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

