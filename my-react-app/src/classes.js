// Classes! 
class Car {
    constructor(name){
        this.brand = name;
    }
    // Methods in the Class
    present() {
        return 'I have a ' + this.brand;
    }
}
// Class Inheritance. 
// To create a class inheritance, use the extends keywords.
// A CLASS created with a CLASS inheritance inherits all the methdods from another class.
class Model extends Car {
    constructor(name, mod){
        super(name);
        this.Model = mod;
    }
    show(){
        return this.present() + ', it is a ' + this.Model
    }
}

// Creating an Object!
// const my_car = new Car("Ford");
// my_car.present();

// inherit the methods from the "Car" class!
const my_car = new Model("Ford", "Mustang");
my_car.show();