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
            runner1 = 0;
            runner2 ++;
        }else {
            runner2 ++;
        }
    }
    while(result.length <= arr.length) {
        if(result[result.length-1] == arr[runner1][0]) {
            result.push(arr[runner1][1]);
            runner1 = 0;
        }else {
            runner1++
        }
    }
    return result.join(" -> ");
}


console.log(mappingItineraries( [  ['ICN', 'LAX'], ['LAX', 'SFO'], ['SJC', 'ICN'], ['NYU', 'SJC'], ['AMS', 'NYU'] ]));
// AMS -> NYU -> SJC -> ICN -> LAX -> SFO

