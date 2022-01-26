class Node{
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}
class SLQueue{
    constructor() {
        this.head = null;
        this.tail = null;
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
        if(!this.head) {
            return null;
        }
        var temp = this.head;
        this.head = this.head.next;
        temp.next = null;
        return temp.value;
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
            while(runner != null){
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
    q_size() {
        var runner = this.head;
        var count = 0;
        while (runner != null){
            count++;
            runner = runner.next;
        }
        return count;
    }
    interleaveQueue(q_two) {
        var q_langth = Math.ceil(this.q_size()/2);
        for (var i = 0; i < q_langth; i++){
            q_two.enqueue(this.dequeue());
        }
        q_langth = q_two.q_size();
        for (var i = 1; i < q_langth; i++){
            q_two.enqueue(q_two.dequeue());
            q_two.enqueue(this.dequeue());
        }
        q_two.displayQueue();
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
q.displayQueue();
var q2 = new SLQueue();
q.interleaveQueue(q2);
q2.displayQueue();
