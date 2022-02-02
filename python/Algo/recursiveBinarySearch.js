function recursiveBinarySearch(list, value, index=0, runner=null){
        if (runner == null){
            runner = Math.floor(list.length/2);
        }else if (runner != null){
            runner = Math.floor(runner/2);
        }
        if (runner == 0){
            console.log(value + " not found");
            return -1;
        }
        if (list[index+runner] == value){
            while (list[index+runner] == value){
                runner += -1;
            }
            index = index + runner + 1;
            console.log("found at index " + index);
            return index;
        }
        if (list[index+runner] < value){
            return recursiveBinarySearch(list, value, index + runner, runner);
        }
        return recursiveBinarySearch(list, value, index , runner);
}


recursiveBinarySearch ([1,1,1,1,1,2,2,2,2,2,2,2,2,2,3,3,4,4,4],2);
recursiveBinarySearch ([1,1,1,1,1,2,3,3,4,4,4],8);
