function circleArea(input){
    let result;
    if (typeof input == 'number'){
        result = (Math.PI * (input**2)).toFixed(2);
    } else {
        result = `We can not calculate the circle area, because we receive a ${typeof input}`;
    }
    console.log(result);
}

circleArea(4);
circleArea("4");
