function solve(matrix){
    let maxNumber = Number.MIN_SAFE_INTEGER;

    matrix.forEach(row => {
        let currentMax = Math.max(...row);
        if (maxNumber < currentMax) {
            maxNumber = currentMax;
        }
    });
    console.log(maxNumber);
}


arr = [[20,50,10],[8, 33 ,145]];
solve(arr);
