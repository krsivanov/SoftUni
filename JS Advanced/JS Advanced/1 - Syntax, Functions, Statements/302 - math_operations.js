function solve(number1, number2, string){
    let result;
    switch(string){
        case '+': result= number1 + number2; break;
        case '-': result= number1 - number2; break;
        case '*': result= number1 * number2; break;
        case '/': result= number1 / number2; break;
        case '%': result= number1 % number2; break;
        case '**': result= number1 ** number2; break;
    }
    console.log(result)
}
