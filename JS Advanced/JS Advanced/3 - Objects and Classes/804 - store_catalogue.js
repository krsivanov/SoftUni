function solve(input){
    let result = {};

    input.forEach(line => {
        let[name, price] = line.split(' : ');

        price =Number(price);
        let letter = name[0];

        if (!result[letter]){
            result[letter]= [];
        }

        let product = {name, price};
        result[letter].push(product);
    });
    let sortedByLetter = Object.entries(result)
                        .sort((curr, next) =>curr[0].localeCompare(next[0]));

    for(let i = 0; i<sortedByLetter.length;i++){
        console.log(sortedByLetter[i][0]);

        let sortByName = sortedByLetter[i][1].sort((curr,next) => curr.name.localeCompare(next.name));
        sortByName.forEach(product => {
            console.log(`  ${product.name}: ${product.price}`);
        })
    }
    
}


solve(['Appricot : 20.4',
'Fridge : 1500',
'TV : 1499',
'Deodorant : 10',
'Boiler : 300',
'Apple : 1.25',
'Anti-Bug Spray : 15',
'T-Shirt : 10']
);
solve(['Banana : 2',
"Rubic's Cube : 5",
'Raspberry P : 4999',
'Rolex : 100000',
'Rollon : 10',
'Rali Car : 2000000',
'Pesho : 0.000001',
'Barrel : 10']);
