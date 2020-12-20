function solve(steps, stepLength, speed) {
    let distanceInMeters = steps * stepLength;
    let speedForMetersInSeconds = speed / 3.6;
    let rest = Math.floor(distanceInMeters / 500);
    let time = distanceInMeters / speedForMetersInSeconds + rest * 60;

    let timeInHours = Math.floor(time / 3600);
    let timeInMins = Math.floor(time/60);
    let timeInSecs = Math.ceil(time % 60);
    
    console.log(`${timeInHours < 10 ? 0 : ""}${timeInHours}:${timeInMins < 10 ? 0 : ""}${timeInMins}:${timeInSecs < 10 ? 0 : ""}${timeInSecs}`)
}


solve(4000, 0.6, 5); 
