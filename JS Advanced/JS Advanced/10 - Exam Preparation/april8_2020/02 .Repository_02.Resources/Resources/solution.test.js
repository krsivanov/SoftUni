let { Repository } = require("./solution.js");
const assert = require('chai').assert;
const expect = require('chai').expect;


describe("Tests …", function () {
    describe("TODO …", function () {
        it("TODO …", function () {
            // TODO: …
        });

        it('getter count', function(){
            const rep = new Repository();
            rep.count = 2
            
            expect(rep.count).to.equal(2);
        })
    });
    // TODO: …
});
