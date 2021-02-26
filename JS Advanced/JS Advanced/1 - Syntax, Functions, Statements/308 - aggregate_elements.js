function solve(input){
    let inputLength = input.length;
    let sum = 0;
    let invSum = 0;
    let concat = '';
    for (i = 0; i< inputLength; i++){
        sum += Number(input[i]);
        invSum += 1/ Number(input[i]);
        concat += input[i].toString();
    }
    console.log(sum);
    console.log(invSum);
    console.log(concat);

}

solve([1,2,3]);
solve([2,4,8,16]);
