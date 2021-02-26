function solve(input){
    let output = '<table>\n';

    let employees = [];

    input.forEach(e => {
        employees.push(JSON.parse(e));
    });

    output += arraysAsTable(employees) + "</table>";
    console.log(output);
    function arraysAsTable(employees) {
        let result = '';
        employees.forEach(employee => {
            result += '\t<tr>\n';
            
            Object.values(employee).forEach(value => {
                result += `\t\t<td>${value}</td>\n`
            })
            result += '\t</tr>\n';
        })
        return result;
    }
}
