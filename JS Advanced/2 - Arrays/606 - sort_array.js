//first solution
function solve(input) {

    input.sort((current, next) => {
        if (current.length > next.length){
            return 1;
        } else if (current.length===next.length){
            return current.localeCompare(next);
        } else {
            return -1;
        }
    }).forEach(e => console.log(e));
    }

//second solution
function solve(input) {
    const twoCriteriasSort = (curr, next) => curr.length -next.length || curr.localeCompare(next);
    input.sort(twoCriteriasSort);
    console.log(input.join('\n')); 
}

solve(['alpha', 'gamma', 'beta']);
solve(['Isacc', 'Theodor', 'Jack', 'Harrison', 'George']);
solve(['test', 'Deny', 'omen', 'Default']);
