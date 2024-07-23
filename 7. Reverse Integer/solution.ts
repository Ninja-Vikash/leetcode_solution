function reverse(x: number): number {
    var numSign = Math.sign(x);
    var str: string = Math.abs(x).toString();
    var newStr: string = str.split("").reverse().join("");

    var newNum: number = Number(newStr);

    if(newNum > 2**31 - 1){
        return 0;
    }

    return newNum * numSign;
};