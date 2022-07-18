console.log('Hello World!!')

// var - legacy code

// let - changeable
let myName = 'Becky';
console.log(myName)

// const - unchangeable
const fullName = 'Rebbecca';
console.log(fullName)

// This will show an error because you cannot declare a new variable when you have already declared full name with const
// fullName = "Rebbecca Jane"

// When using the let function you can declare new variables
myName = 'Bfoxy';
console.log(myName)

// if statements in JavaScript are very similar to Python in the way that they are used. However, the syntax is slightly different.

if (myName === 'Becky') {
    console.log('Hello Becky')
}else if (myName === 'Bfoxy') {
    console.log('Hello BFoxy')
} else {
    console.log('Who are you?')
}

// Functions 
function sayHello() {
    console.log('Hello')
}
sayHello()