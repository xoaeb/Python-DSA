class myNode {
  value: number;
  next: myNode | null;
  constructor(value: number) {
    this.value = value;
    this.next = null;
  }
}

class myStack {
  top: myNode | null;
  height: number;
  constructor(value: number) {
    const newNode = new myNode(value);
    this.top = newNode;
    this.height = 1;
  }

  printStack() {
    let temp = this.top;
    while (temp) {
      console.log(temp.value);
      temp = temp.next;
    }
  }
}
