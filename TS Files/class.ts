class DefaultRoom {
  height: number;
  width: number;
  name: string;

  constructor(height: number, width: number, name: string) {
    this.height = height;
    this.width = width;
    this.name = name;
  }

  area() {
    console.log(
      `area of the  ${this.name} room is: ` + this.height * this.width
    );
    return this.height * this.width;
  }

  operation(operation: string) {
    return `operation of the  ${this.name} room is:  ${operation} `;
  }
}

const room1 = new DefaultRoom(10, 20, "Bedroom");
// room1.area();

const room2 = new DefaultRoom(8, 9, "Kitchen");
const kitchenArea = room2.area();

const kitchenOperation = room2.operation("cooking");
console.log(kitchenOperation);

// console.log(kitchenArea);
