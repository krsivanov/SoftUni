function squareOfStars(input = 5){
    let n = Number(input)
    result = ''
    for(i=0;i<n; i++){
        for(j=0;j<n;j++){
            result += '* ';
        }
        result += '\n';
    }
    console.log(result);
}

squareOfStars(3);
