// return masked string
function maskify(cc) {
    var ccc = String(cc);
    var x = "";
    for (var i = 0;i < ccc.length;i++){
        var z =  ccc.length - 4;
        if (i < z){
            x = x + '#';
        }
        else{
            x = x + ccc[i];
        }
    }
    return x;
}

console.log(maskify('464356328793874683568992436579'));
