function Fizzbuzz() {
  this.isDivisibleByThree = function(number) {
    return number % 3 === 0;
  };

  this.isDivisibleByFive = function(number) {
    return number % 5 === 0;
  };

  this.isDivisibleByFifteen = function(number) {
    return number % 15 === 0;
  };
}