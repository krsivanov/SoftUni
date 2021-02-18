class Parking {
    constructor(capacity) {
        this.capacity = capacity;
        this.vehicles = [];
    }

    addCar(carModel, carNumber) {
        if (this.capacity <= 0) {
            throw new Error(`Not enough parking space.`)
        }

        this.vehicles.push({ carModel, carNumber, payed: false })
        this.capacity--;
        return `The ${carModel}, with a registration number ${carNumber}, parked.`
    }

    removeCar(carNumber) {
        const curCar = this.vehicles.find(v => v.carNumber == carNumber);

        if (!curCar) {
            throw new Error(`The car, you're looking for, is not found.`)
        }

        if (!curCar.payed) {
            throw new Error(`${carNumber} needs to pay before leaving the parking lot.`)
        }

        for (const index in this.vehicles) {
            if (this.vehicles[index].carNumber == carNumber) {
                this.vehicles.splice(index, 1)
            }
        };

        this.capacity++;
        return `${carNumber} left the parking lot.`
    }

    pay(carNumber) {
        const curCar = this.vehicles.find(v => v.carNumber == carNumber);

        if (!curCar) {
            throw new Error(`${carNumber} is not in the parking lot.`)
        }

        if (curCar.payed) {
            throw new Error(`${carNumber}'s driver has already payed his ticket.`)
        }

        curCar.payed = true;
        return `${carNumber}'s driver successfully payed for his stay.`
    }

    getStatistics(carNumber) {
        if (carNumber) {
            const car = this.vehicles.find(c => c.carNumber == carNumber);
            return `${car.carModel} == ${carNumber} - ${car.payed ? 'Has payed' : 'Not payed'}`;
        }

        let result = [`The Parking Lot has ${this.capacity} empty spots left.`]
        this.vehicles.sort((a, b) => a.carModel.localeCompare(b.carModel))

        for (const car of this.vehicles) {
            result.push(`${car.carModel} == ${car.carNumber} - ${car.payed ? 'Has payed' : 'Not payed'}`)
        }

        return result.join('\n')
    }
}