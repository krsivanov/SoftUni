const assert = require('chai').assert;
const expect = require('chai').expect;
const dealership = require('./dealership');

describe('test', () => {
    describe('returnOldCar', () => {
        //model is supported -> price reduced by model value
        //model is not supported -> no discount
        it('returns orginal price when model unsupported', () => {
            expect(dealership.newCarCost('a',1)).to.equal(1);
        });
        
        it('returns discounted price', () => {
            expect(dealership.newCarCost('Audi A4 B8',30000)).to.equal(15000);
        });
    });

    describe('carEquipment', () => {
        it ('single element, single pick', () =>{
            expect(dealership.carEquipment(['a'], [0])).to.deep.equal(['a'])
        })

        it ('single element, single pick', () =>{
            expect(dealership.carEquipment(['a','b','c'], [0,2])).to.deep.equal(['a', 'c'])
        })

        it ('single element, single pick', () =>{
            expect(dealership.carEquipment(['a','b','c'], [1])).to.deep.equal(['b'])
        })
        //single elment , single pick
        //test overloading - multiple elements, multiple picks
    });

    describe('euroCategory', () => {
        it('category is below threshold', () => {
            expect(dealership.euroCategory(1)).to.equal('Your euro category is low, so there is no discount from the final price!');
        })

        it('category is above threshold', () => {
            expect(dealership.euroCategory(5)).to.equal(`We have added 5% discount to the final price: 14250.`);
        })

        it ('category is oat threshold (edge case)', () => {
            expect(dealership.euroCategory(4)).to.equal(`We have added 5% discount to the final price: 14250.`)
        })
        //category is bellow threshold
        //category is above threshold
        //category is at thershold(edge case )
    });
})
 