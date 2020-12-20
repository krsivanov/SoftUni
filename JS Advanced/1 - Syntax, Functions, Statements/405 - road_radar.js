function solve(input){
    let speedLimit=0;
    currentSpeed = Number(input[0]);
    area = input[1];
    switch(area){
        case 'motorway':
            speedLimit = 130;
            break;
        case 'interstate':
            speedLimit = 90;
            break;
        case 'city':
            speedLimit = 50;
            break;
        case 'residential':
            speedLimit = 20;
            break;
    }
    if ((currentSpeed-speedLimit)>40){
        console.log('reckless driving');
    } else if((currentSpeed-speedLimit)>20 && (currentSpeed-speedLimit)<=40){
        console.log('excessive speeding');
    } else if((currentSpeed-speedLimit)>0 && (currentSpeed-speedLimit)<=20){
        console.log('speeding');
    }
}

solve(40, 'city');
solve(21, 'residential');
solve(120, 'interstate');
solve(200, 'motorway');
