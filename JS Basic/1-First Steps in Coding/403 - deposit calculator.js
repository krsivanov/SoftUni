function solve(depositedSum, monthlyTerm, interestRate){
    depositedSum = Number(depositedSum);
    term = Number(monthlyTerm);
    interestRate = Number(interestRate);

    let totalInterest = depositedSum * (interestRate/100);
    totalInterest = totalInterest /12;
    let result = depositedSum + term * totalInterest;
    console.log(result)
}
