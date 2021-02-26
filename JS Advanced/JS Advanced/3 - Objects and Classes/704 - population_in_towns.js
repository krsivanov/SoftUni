function solve(input){
    let result = input
        .map(x => x.split(' <-> '))
        .map(x => [x[0], Number(x[1])])
        .reduce(
            (a,x) => {
                let currentTown = x[0];
                let currentPopulation = x[1]
                if (!a.hasOwnProperty(currentTown)){
                    a[currentTown] = 0;
                }
                a[currentTown] += currentPopulation;

                return a;
            },
            {}
            )
    for (const town in result) {
        console.log(town + ' : '+result[town]);
            
        
    }
}

solve(['Sofia <-> 1200000',
'Montana <-> 20000',
'New York <-> 10000000',
'Washington <-> 2345000',
'Las Vegas <-> 1000000']
);
solve(['Istanbul <-> 100000',
'Honk Kong <-> 2100004',
'Jerusalem <-> 2352344',
'Mexico City <-> 23401925',
'Istanbul <-> 1000']
);
