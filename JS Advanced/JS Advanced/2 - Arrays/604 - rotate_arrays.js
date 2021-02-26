function solve(input){
    let count = input.pop();

    for(let i=0; i<count% input.length;i++){
        let lastElement = input.pop();
        input.unshift(lastElement)
    }
    console.log(input.join(' '));
}


solve(['1', '2', '3', '4', '2']);
solve(['Banana', 'Orange', 'Coconut', 'Apple', '15']);
