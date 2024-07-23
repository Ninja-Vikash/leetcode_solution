/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    var numSign = Math.sign(x);
    var str = Math.abs(x).toString();
    var newStr = str.split("").reverse().join("");

    var newNum = Number(newStr);

    if(newNum > 2**31 - 1){
        return 0;
    }

    return newNum * numSign;
};