class MyNode {
  value: number;
  next: MyNode | null;
  prev: MyNode | null;

  constructor(value: number) {
    this.value = value;
    this.next = null;
    this.prev = null;
  }
}

class DoublyLinkedList {
  head: MyNode | null;
  tail: MyNode | null;
  length: number;
  constructor(value: number) {
    const newNode = new MyNode(value);
    this.head = newNode;
    this.tail = newNode;
    this.length = 1;
  }
  printList() {
    let temp = this.head;
    // while (temp !== null) {
    //   console.log(temp.value);
    //   temp = temp.next;
    // }

    for (let i = 0; i < this.length; i++) {
      console.log(temp!.value, `[${i}]`);
      temp = temp!.next;
    }
  }

  append(value: number) {
    const newNode = new MyNode(value);
    if (this.length === 0) {
      this.head = newNode;
      this.tail = newNode;
    } else {
      if (this.tail) {
        this.tail.next = newNode;
        newNode.prev = this.tail;
        this.tail = newNode;
      }
    }
    this.length++;
    return true;
  }

  pop() {
    if (this.length === 0) return null;
    const temp = this.tail;
    if (this.length === 1) {
      this.head = null;
      this.tail = null;
      this.length--;
    } else {
      const prev = temp!.prev;
      prev!.next = null;
      temp!.prev = null;
    }
    this.length--;
    return temp;
  }

  prepend(value: number): boolean {
    const newNode = new MyNode(value);
    if (this.length === 0) {
      this.head = newNode;
      this.tail = newNode;
    } else {
      newNode.next = this.head;
      if (this.head) this.head.prev = newNode;
      this.head = newNode;
    }
    this.length += 1;
    return true;
  }

  popFirst(): number | null {
    if (this.length === 0) {
      return null;
    }
    let temp = this.head;
    if (this.length === 1) {
      this.head = null;
      this.tail = null;
    } else {
      if (this.head) {
        this.head = this.head.next;
        if (this.head) this.head.prev = null;
      }
      temp!.next = null;
    }
    this.length -= 1;
    return temp!.value;
  }

  get(index: number) {
    if (index < 0 || index >= this.length) return null;

    let temp = this.head;
    if (index < this.length / 2) {
      for (let i = 0; i < index; i++) {
        temp = temp!.next;
      }
    } else {
      temp = this.tail;
      for (let i = this.length - 1; i > index; i--) {
        temp = temp!.prev;
      }
    }
    return temp;
  }
}

const myDoublyLinkedList = new DoublyLinkedList(10);
myDoublyLinkedList.append(15);
myDoublyLinkedList.append(25);
myDoublyLinkedList.append(40);
myDoublyLinkedList.append(46);
myDoublyLinkedList.append(50);
myDoublyLinkedList.append(55);
myDoublyLinkedList.append(60);
myDoublyLinkedList.append(65);
myDoublyLinkedList.append(70);
myDoublyLinkedList.append(75);

// const poppedNode: any = myDoublyLinkedList.pop();
myDoublyLinkedList.printList();
// console.log(poppedNode.value, "<<<<<<<<");

const gettedNode: MyNode | any = myDoublyLinkedList.get(6);
console.log(gettedNode.value, "<<<<<<<<");
