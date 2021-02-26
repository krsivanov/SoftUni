function solve(input){
    // let output = [];
    let max = Number.MIN_SAFE_INTEGER;

    // input.forEach(num => {
    //     if (num>=max){
    //         max = num;
    //         console.log(max);
    //     }
    // });
    let output = input.reduce((acc, curr) =>{
        if(curr>=max){
            max =curr;
            acc.push(max);
        }
        return acc;
    }, []);
    console.log(output.join('\n'));
}

solve([1, 3, 8, 4, 10, 12, 3, 2, 24]);
solve([1, 2, 3, 4]);
solve([20, 3, 2, 15, 6, 1]);
