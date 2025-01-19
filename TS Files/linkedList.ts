// NodeClass Class
 class NodeClass {
  value: number;
  next: NodeClass | null;

  constructor(value: number) {
    this.value = value;
    this.next = null;
  }
}

// LinkedList Class
class LinkedList {
  head: NodeClass | null;
  tail: NodeClass | null;
  length: number;

  constructor(value: number) {
    const newNode = new NodeClass(value);
    this.head = newNode;
    this.tail = newNode;
    this.length = 1;
  }

  // Print all nodes in the list
  printList(): void {
    let temp = this.head;
    while (temp !== null) {
      console.log(temp.value);
      temp = temp.next;
    }
  }

  // Append a node to the end of the list
  append(value: number): boolean {
    const newNode = new NodeClass(value);
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

  // Pop the last node
  pop(): NodeClass | null {
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

  // Prepend a node to the start
  prepend(value: number): boolean {
    const newNode = new NodeClass(value);
    if (this.length === 0) {
      this.head = newNode;
      this.tail = newNode;
    } else {
      newNode.next = this.head;
      this.head = newNode;
    }
    this.length++;
    return true;
  }

  // Pop the first node
  pop_first(): NodeClass | null {
    if (this.length === 0) return null;

    const temp = this.head;
    if (this.head !== null) {
      this.head = this.head.next;
    }
    if (temp !== null) temp.next = null;

    this.length--;
    if (this.length === 0) {
      this.tail = null;
    }

    return temp;
  }

  // Get node at an index
  get(index: number): NodeClass | null {
    if (index < 0 || index >= this.length) return null;
    let temp = this.head;
    for (let i = 0; i < index; i++) {
      if (temp !== null) temp = temp.next;
    }
    return temp;
  }

  // Set value of a node at an index
  set_value(index: number, value: number): boolean {
    const temp = this.get(index);
    if (temp) {
      temp.value = value;
      return true;
    }
    return false;
  }

  // Insert node at an index
  insert(index: number, value: number): boolean {
    if (index < 0 || index > this.length) return false;
    if (index === 0) return this.prepend(value);
    if (index === this.length) return this.append(value);

    const newNode = new NodeClass(value);
    const temp = this.get(index - 1);

    if (temp !== null) {
      newNode.next = temp.next;
      temp.next = newNode;
    }

    this.length++;
    return true;
  }

  // Remove node at an index
  remove(index: number): NodeClass | null {
    if (index < 0 || index >= this.length) return null;
    if (index === 0) return this.pop_first();
    if (index === this.length - 1) return this.pop();

    const pre = this.get(index - 1);
    const temp = this.get(index);

    if (pre !== null && temp !== null) {
      pre.next = temp.next;
      temp.next = null;
    }

    this.length--;
    return temp;
  }

  // Reverse the linked list
  reverse(): void {
    let temp = this.head;
    let before: NodeClass | null = null;
    let after: NodeClass | null = null;
    this.tail = this.head;

    while (temp !== null) {
      after = temp.next;
      temp.next = before;
      before = temp;
      temp = after;
    }

    this.head = before;
  }
}

// Example Usage
const myLinkedList = new LinkedList(5);
myLinkedList.append(9);
myLinkedList.append(39);
myLinkedList.prepend(1);
myLinkedList.printList();
console.log("Reversing list...");
myLinkedList.reverse();
myLinkedList.printList();
