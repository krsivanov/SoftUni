function area() {
    return Math.abs(this.x * this.y);
};
function vol() {
    return Math.abs(this.x * this.y * this.z);
};


const example1 = '[{"x":"1","y":"2","z":"10"},{"x":"7","y":"7","z":"10"},{"x":"5","y":"2","z":"10"}]';

const example2 = '[{"x":"10","y":"-22","z":"10"},{"x":"47","y":"7","z":"-5"},{"x":"55","y":"8","z":"0"},{"x":"100","y":"100","z":"100"},{"x":"55","y":"80","z":"250"}]';





function solve(area, vol, dataAsJSON){
    const figures = JSON.parse(dataAsJSON);
    
    const result = [];

    for (let figure of figures) {
        const output = {
            area: area.call(figure),
            volume: vol.call(figure)
        };
        result.push(output);
    }
    return result;
}

console.log(solve(area, vol , example1));
