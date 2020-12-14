function convertor(radians){
    let pi = Math.PI;
    let fixed = pi.toFixed(2);
    let degrees = radians *180 / pi;
    
    console.log(degrees.toFixed(2));
    // console.log(degrees.ceil(degrees))
}
