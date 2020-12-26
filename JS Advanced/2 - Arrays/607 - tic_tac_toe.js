function solve(input){

    let dashboard = [
        [false, false, false],
        [false, false, false],
        [false, false, false]
    ];
    let player = 'X';
    input.forEach(line => {
        let [row, col] = line.split(' ').map(num => Number(num));
        dashboard[row][col] = player;
        player = player === 'X' ? 'O' : 'X';
        console.log();
    });
}

solve(["0 1",
"0 0",
"0 2", 
"2 0",
"1 0",
"1 1",
"1 2",
"2 2",
"2 1",
"0 0"]);

solve(["0 0",
"0 0",
"1 1",
"0 1",
"1 2",
"0 2",
"2 2",
"1 2",
"2 2",
"2 1"]);

solve(["0 1",
"0 0",
"0 2",
"2 0",
"1 0",
"1 2",
"1 1",
"2 1",
"2 2",
"0 0"]);
