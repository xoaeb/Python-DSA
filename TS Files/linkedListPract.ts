class MyNode {
  value: number;
  next: MyNode | null;

  constructor(value: number) {
    this.value = value;
    this.next = null;
  }
}

class MyLinkedList {
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
    while (temp !== null) {
      console.log(temp.value);
      temp = temp.next;
    }
  }

  append(value: number) {
    const newNode = new MyNode(value);
    if (this.length === 0) {
      this.head = newNode;
      this.tail = newNode;
    } else {
      if (this.tail !== null) {
        this.tail.next = newNode;
      }
      this.tail = newNode;
    }
    this.length++;
    return true;
  }

  pop() {
    if (this.length === 0) return null;
    let temp = this.head;
    let pre = this.head;
    while (temp !== null && temp.next !== null) {
      pre = temp;
      temp = temp.next;
    }
    if (pre !== null) {
      this.tail = pre;
      this.tail.next = null;
    }

    this.length--;

    if (this.length === 0) {
      this.head = null;
      this.tail = null;
    }

    return temp;
  }

  prepend(value: number) {
    const newNode = new MyNode(value);
    if (this.length === 0) {
      this.head = newNode;
      this.tail = newNode;
    } else {
      if (this.head !== null) {
        newNode.next = this.head;
      }
      this.head = newNode;
    }
  }

  popFirst() {
    if (this.length === 0) return null;
    const temp = this.head;
    if (this.length === 1) {
      this.head = null;
      this.tail = null;
      this.length--;
      return temp;
    } else {
      if (this.head !== null && temp !== null) {
        this.head = this.head.next;
        temp.next = null;
      }
      this.length--;
      return temp;
    }
  }

  get(index: number) {
    if (index < 0 || index >= this.length) return null;
    let temp = this.head;
    for (let i = 0; i < index; i++) {
      if (temp !== null) temp = temp.next;
    }
    return temp;
  }
  setValue(index: number, value: number) {
    let temp = this.get(index);
    if (temp) {
      temp.value = value;
      return true;
    }
    return false;
  }

  insert(index: number, value: number) {
    if (index < 0 || index > this.length) {
      return null;
    } else if (index === 0) {
      return this.prepend(value);
    } else if (index === this.length) {
      return this.append(value);
    }

    const newNode = new MyNode(value);
    const temp = this.get(index - 1);

    if (temp) {
      newNode.next = temp.next;
      temp.next = newNode;
    }
    this.length++;
  }
  removeWithIndex(index: number) {
    if (index < 0 || index >= this.length) {
      return null;
    } else if (index === 0) {
      return this.popFirst();
    } else if (index === this.length -1) {
      return this.pop();
    }
    let pre = this.get(index - 1);
    let temp = pre?.next;
    if (temp && pre) {
      pre.next = temp.next;
      temp.next = null;
    }
    this.length--;
    return temp;
  }
}
const newLL = new MyLinkedList(10);
newLL.append(15);
newLL.append(16);
newLL.append(17);
newLL.append(18);

// newLL.printList();
// const poppedNode = newLL.pop();
// console.log(poppedNode.value, "poppedNode");
// newLL.prepend(1);
newLL.printList();

// const poppedNode = newLL.popFirst();
// console.log(poppedNode?.value, "poppedNode");
// newLL.printList();
// const getByIndex = newLL.get(2);
// console.log(getByIndex?.value, "getByIndex");

// newLL.setValue(2, 99);
// newLL.printList();
// newLL.insert(2, 13);
// newLL.printList();
newLL.removeWithIndex(1);
newLL.printList();
