function solve(n) {
    let i=0;
    let sum = 0;
    let counter = 0;
    while (i<n){
        if (counter % 2 != 0){
            i++;
            sum = sum + counter;
            console.log(counter);
        }
        counter++;
    }
    console.log(`Sum: ${sum}`);
}

solve(5);
