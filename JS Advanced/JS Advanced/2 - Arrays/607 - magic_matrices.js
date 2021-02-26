function solve(input) {
    let sums = [];
    for (let i = 0; i < input.length; i++) {
        let columnSum = 0;
        sums.push(input[i].reduce((accumulator, value) => accumulator + value));
        for (let j = 0; j < input.length; j++) {
            columnSum += input[j][i];
        }
        sums.push(columnSum);
    }
    let isEqual = Math.max(...sums) === Math.min(...sums);
    console.log(isEqual);
}
