function solve(input) {

    let result = {};
    let juicesInOrder = {};

    input.forEach(line => {
        let [product, quantity] = line.split(' => ');

        if (!result[product]) {
            result[product] = Number(quantity);
        } else {
            result[product] += Number(quantity);
        }
        if (result[product]>= 1000){
            juicesInOrder[product] = 0;
        }
    });

    Object.keys(result).forEach(j => {
        if (juicesInOrder[j] !== undefined){
            juicesInOrder[j] += parseInt(result[j] /1000);
        }
    })

    Object.keys(juicesInOrder).forEach(j => console.log(`${j} => ${juicesInOrder[j]}`));
}

solve(['Orange => 2000',
    'Peach => 1432',
    'Banana => 450',
    'Peach => 600',
    'Strawberry => 549']);

solve(['Kiwi => 234',
    'Pear => 2345',
    'Watermelon => 3456',
    'Kiwi => 4567',
    'Pear => 5678',
    'Watermelon => 6789']);
