function sum(n,m){
    let sum = 0;
    let num1 = Number(n);
    let num2 = Number(m);
    for (let i=num1; i<=num2 ; i++){
        sum += i;
    }
    console.log(sum);
}

sum('1', '5')
