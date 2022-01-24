class Node{
    constructor(value) {
        this.value = value
        this.next = null
    }
}
class SLQueue{
    constructor() {
        this.head = null
        this.tail = null
    }
    enqueue(value) {
        var newNode = new Node(value);
        if (this.head == null){
            this.head = newNode;
            this.tail = newNode;
            return this;
        }else {
            this.tail.next = newNode;
            this.tail = newNode;
            return this;
        }
    }
    dequeue() {
        var x = this.head;
        this.head = this.head.next;
        x.next = null;
        return x.value;
    }
    contains(value) {
        var runner = this.head;
        while(runner != null) {
            if(runner.value === value) {
                console.log("true");
                return true;
            }
            runner = runner.next;
        }
        console.log("false");
        return false;
    }
    displayQueue() {
            var runner = this.head;
            var str = "queue start -- ";
            while(runner){
                str += runner.value + " --> ";
                runner = runner.next;
            }
            str += "null --";
            console.log(str);
    }
    front() {
        console.log(this.head.value);
        return this.head.value;
    }
    isEmpty() {
        if(this.head == null) {
            console.log("empty");
            return true;
        }else {
            console.log("not empty");
            return false;
        }
    }
}

var q = new SLQueue();
q.enqueue(1);
q.enqueue(2);
q.enqueue(3);
q.enqueue(4);
q.enqueue(5);
q.enqueue(6);
q.enqueue(7);
q.enqueue(8);
q.displayQueue();
q.dequeue();
q.displayQueue();
q.contains(5);
q.contains(9);
q.front();
q.isEmpty();
