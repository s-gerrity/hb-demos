// This covers some advanced concepts around "this"
//
// Joel Burton <joel@joelburton.com>
//
// (Updates to arrow functions are not by Joel)

// Normally, this is "the object being built" in a constructor
// function, like so:

class Cat {
  constructor(name) {
    this.name = name;
    this.hunger = 10;
  }
}

// But any function can have refer to "this":

function sayMessage() {
    console.log("Important: " + this.secretMessage);
}

// If you just called this directly, it will use a
// "default this" (which, somewhat oddly, is the JS 'window'
// object, the default context for JS). So it won't find
// any .secretMessage attrib.

// We could make an object with such an attribute:

let telegram = {secretMessage: 'Meow!'};

// But we can't just try to "call that function on our object":
//

// telegram.sayMessage();  //  can't find sayMessage

// We could put sayMessage on telegram as a new attribute:

telegram.sayMessage = sayMessage;

//
// and now we could get to it, as we'd expect:

telegram.sayMessage(); //  <--- works! "Meow"

// However, for one-off things, JS provides a ".call()"
// function, which says "call this function using this
// object as its this"

sayMessage.call(telegram);    // works!

// .call() takes variable additional arguments, which
// become the arguments told the function (ie, if
// sayMessage took arguments, we could pass them that
// way:
//
//    sayMessage.call(telegram, arg1, arg2, ...)

// There's also ".apply()", which lets you pass those
// extra args as a list:
//
//    sayMessage.apply(telegram, [arg1, arg2])
//
// This form is particularly useful when you combine with
// "arguments", a magical variable that means "the arguments
// given to this function, the one we're in". You can read
// about this separately. This becomes useful if you want
// to build something like Python's "super().myfunc(*args)".
// See `cats-inheritance.js` for an example.
//
// (Slightly more obscurely, there's "fn.bind(obj)", which
// returns a new function permanently bound to this
// context, so it always considers that object to be
// it's context. if wanted this, we'd say:
//    var telegramMessager = sayMessage.bind(telegram)
// and then we could just call telegramMessenger, knowing
// it would always be bound to that telegram object, so
// we didn't have to .call or .apply it each time.
// In my experience, this is pretty rare.)


// So, effectively, this whole business with .call() or
// .apply() says "I want to provide a special 'this'
// context when I call this function.

// ===================

// "this" isn't a normal variable -- it's always this "context".
// This kicks in we try to do something like:

class CatNotifyBad {
  constructor(name) {
    this.name = name;

    setTimeout(function () {
      console.log("A second ago, I created " + this.name);
    }, 1000);
  }
}
/* end contextual this example */

// (the use of setTimeout() here is just an arbitrary example
// but the problem described would be the same for any enclosed
// function, so we'd have this same problem with an event callback,
// an AJAX success function, recursion, a closure, etc.)

// In *theory*, when I make a cat like:

const audenBad = new CatNotifyBad("Auden");

// it would tell me one second later that it had made Auden.

// However, inside of that setTimeout function, it has it's *own*
// idea of what "this" is (which is that same "default this" --- the
// JS window object).
//
// As such, in that console.log(), "this" isn't our new cat
// anymore (our cat is fine, it's just that "this' isn't pointing
// to it). So we won't get the new cat's name, it will look for
// a "name" attribute on the window object (and unless you've
// put one there, it won't find anything, so this will say
// "I created undefined")

// [Tiny detail for the pycharm users: notice how PyCharm lights
// up "this" in the code above as probably wrong? PyCharm rocks.]

// We can solve this by writing our callback as an arrow function. This is
// difference between arrow functions and regular functions.
//
// Arrow functions don't have a contextual "this". This is why people prefer
// using the arrow function syntax for callbacks.

class CatNotifyGood {
  constructor(name) {
    this.name = name;

    setTimeout(() => {
      console.log(`A second ago, I created ${this.name}`);
    }, 1000);
  }
}
/* end arrow function example */

const audenGood = new CatNotifyGood('Auden');

// In the dark old days, people got around "this" contextual-this problem (haha)
// by binding "this" to a new variable.
//
// So you might have seen:
//
//     let that = this;
// or
//     let self = this;
//
/// ... and now you know why :)
