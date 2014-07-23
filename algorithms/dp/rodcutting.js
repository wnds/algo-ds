//Given a rod of length n inches and a table of prices pi for i D 1; 2; : : : ; n, 
//determine the maximum revenue rn obtain- able by cutting up the rod and selling the pieces. 
//Note that if the price pn for a rod of length n is large enough, an optimal solution may require no cutting at all.
//Comlexity : O(n^2)
//run: node rodcutting.js 5
//debug: node-inspector && node --debug-brk rodcutting.js
var priceData = {
    1: 1,
    2: 5,
    3: 8,
    4: 9,
    5: 10,
    6: 17,
    7: 19,
    8: 21,
    9: 24,
    10: 30
};
var revenues = {
    0: 0
};
var pieces = [];
//console.log("Input price matrix : " + JSON.stringify(priceData));
var rodLength = process.argv[2];
if (rodLength == undefined || rodLength > 10) {
    console.log("Provide rodlength for which optimal price should be calculted as input. it should be <= 10");
    return;
}
for (var i = 1; i <= rodLength; i++) {
    var revenue = -1;
    for (var smallPieceLength = 1; smallPieceLength <= i; smallPieceLength++) {
        //console.log(i + ' ' + smallPieceLength + ' ' + revenue + " " + priceData[smallPieceLength] + ' ' + revenues[i - smallPieceLength]);
        if (revenue != -1 && revenue < (priceData[smallPieceLength] + revenues[i - smallPieceLength])) {
            pieces = [];
            pieces.push(smallPieceLength);
            (i - smallPieceLength) > 0 ? pieces.push(i - smallPieceLength) : false;
        }
        revenue = Math.max(revenue, priceData[smallPieceLength] + revenues[i - smallPieceLength]);
    };
    revenues[i] = revenue;
};
console.log("Maximum revenue from rod of length " + rodLength + " is " + revenues[rodLength] + " with pieces cut as " + JSON.stringify(pieces));