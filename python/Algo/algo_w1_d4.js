function bookIndex(arr){
    var str = "";
    for (i = 0 ; i < arr.length ; i++){
        if (i != 0 && str[str.length - 1] != " "){
            str = str + " ";
        }
        if (arr[i + 1] == arr[i] + 1){
            var x = arr[i];
            //var j = i;
            while (arr[i + 1] == arr[i] + 1){
                i++;
            }
            var z = arr[i];
            str = str + x + "-" + z;
            //i = j;
        }
        else if (arr[i] != str[str.length - 2]){
            str = str + arr[i];
        }
    }
    return str;
}

console.log(bookIndex([1,3,4,5,7,8,10,12]));
console.log(bookIndex([1,2,3,4,6,8,9,10,11,12]));
