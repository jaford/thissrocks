/* 
Arrow functions

This allows us to write shorter functions syntax
*/

// Before
hello = function(){
    return "Hello World!";
}

// With Arrow Functions 
hello = () => {
    return "Hello World 2!"
}

/* 
In some cases you can even get this shorter.

If the function only has one statement, and the statement returns a value,
you can remove the brackets and the return Keyword: 
*/
hello = () => "Hello World 3!";

// If you have parameters, you pass them inside the perentheses
hello = (val) => "Hello World 4!" + val;

/* 
The handling of "this" is also very differnt in arrow functions

In short, with arrow function there is no binding of "this".

The first example will use a regular functon. Then the second 
function with be using arrow function.  
*/
// With Regular Function
class Header_1 {
    constructor() {
        this.color = "Red";
    }
    //Regular Function
    changeColor = function() {
        document.getElementById("Demo").innerHTML += this;
    }
}

const myheader_1 = new Header();

// The window object calls the function
window.addEventListener("load", myheader.changeColor);

// A button object calls the function: 
document.getElementById("btn").addEventListener("click", myheader.changeColor);

// With arrow function 
class Header_2 {
    constructor() {
        this.color = "Red";
    }
    //Arrow Function
    changeColor = () => {
        document.getElementById('Demo').innerHTML += this;
    }
}

const myheader_2 = new Header();

// The window object calls the function
window.addEventListener("load", myheader_2.changeColor);

// A button object calls the function: 
document.getElementById("btn").addEventListener("click", myheader_2.changeColor);

