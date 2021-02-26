function stringLength(firstString, secondString, thirdString){
    let sumLength;
    let averageLength;

    sumLength = firstString.length +secondString.length+ thirdString.length;
    console.log(sumLength);
    averageLength = Math.floor(sumLength/3);
    console.log(averageLength)
}

stringLength('chocolate', 'ice cream', 'cake');
