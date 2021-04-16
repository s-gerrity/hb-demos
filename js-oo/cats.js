"use strict";

// ============================================================
// Demo ES6 classes
//
// Joel Burton <joel@joelburton.com>


// Standard cat class:
/* start Cat class*/
class Cat {
  constructor(name) {
    this.name = name;
    this.hunger = 10;
  }
  // end Cat constructor (this comment is used for generating handouts!)
  
  // start Cat methods
  greet() {
    return `Meow, I'm ${this.name}`;
  }
  // end Cat.greet

  feed(calories) {
    this.hunger -= calories;
    return `Om nom nom, I <3 ${this.food}`;
  }
}
/* end Cat class*/

// Sadly, there's no way to add a class attribute with this new syntax
// directly (this comes in ES7). You can still do this the old-fashioned way:

Cat.prototype.food = 'kibble';

const ezra = new Cat('Ezra');

// ============================================================
// Subclassing

/* start FrenchCat */
class FrenchCat extends Cat {
  constructor(name) {
    super(name);  // Call our parent's constructor
    this.hunger = 20;
  }
  /* end FrenchCat constructor */

  /* start FrenchCat methods */
  greet() {
    // Use super to call our parent's method
    return `Bonjour and ${super.greet()}`;
  }
  /* end FrenchCat.greet */

  // A "getter" property --- this acts like a simple
  // property but it run this code. Use this with
  //
  //    pierre.doubleHunger   // no ()

  get doubleHunger() {
    return this.hunger * 2;
  }

  // A static method --- you can call this on
  // the FrenchCat class itself, like
  //
  //    FrenchCat.kibbleToCal(10);
  //
  // or on a french cat:
  //
  //    pierre.kibbleToCal(10);

  static kibbleToCal(kibble) {
    return kibble * .12345;
  }
}
/* end FrenchCat */

// Override the class attribute; french cats eat brie

FrenchCat.prototype.food = 'brie';

const pierre = new FrenchCat('Pierre');


// ============================================================
// A simpler subclass

/* start SpanishCat */
class SpanishCat extends Cat {

  greet() {
    return `Hola, I'm ${this.name}`;
  }

  salsa() {
    return "cha cha cha";
  }
}
/* end SpanishCat */

SpanishCat.prototype.food = 'tapas';

const consuela = new SpanishCat('Consuela');

// ============================================================
// Call freestanding functions using object context

function enfur(color) {
  console.log('fur, fur, fur');
  return `${this.name} has covered you in ${color} fur`;
}

function chaseLaserPointer() {
  return this.name + " chases lasers!";
}

chaseLaserPointer.call(ezra);        // "Ezra chases lasers!"
enfur.call(ezra, "orange");      // "Ezra has covered you in orange fur."
enfur.apply(ezra, ["orange"]);   // "Ezra has covered you in orange fur."

// Make a function that will use the ezra object context
let ezraChasesLasers = chaseLaserPointer.bind(ezra);

ezraChasesLasers();       // "Ezra chases lasers!"
