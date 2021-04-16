describe("My Test Suite", function () {

    it("should add numbers", function () {
        var sum = adder(2, 3);
        expect(sum).toBe(5);
    });

    it("should add negative numbers", function () {
        expect(adder(1, -1)).toBe(99);
    });

});
