class Node {
    constructor(value) {
        this.value = value
        this.next = null
    }
}

class SLStack {
    constructor() {
        this.top = null
    }

    push(value) {
        var newNode = new Node(value)
        newNode.next = this.top
        this.top = newNode
        console.log(newNode.value + " added to the stack")
        return this;
    }

    pop() {
        var x = this.top
        this.top = this.top.next
        x.next = null
        console.log(x.value + " removed from the stack")
        return x.value
    }

    returnTop() {
        console.log(this.top.value + " is the top of the stack")
        return this.top.value
    }

    stackSize() {
        var runner = this.top
        var count = 0
        while (runner != null) {
            count++
            runner = runner.next
        }
        console.log(count + " is the stack size")
        return count
    }

    printStack() {
        var runner = this.top
        var str = "top of the stack " + runner.value
        while (runner.next != null) {
            str += " --> " + runner.next.value
            runner = runner.next
        }
        console.log(str + " end of the stack")
        return str
    }
}

var sls = new SLStack()
sls.push(3)
sls.push(18)
sls.push(12)
sls.push(78)
sls.push(56)
sls.pop()
sls.returnTop()
sls.printStack()
sls.stackSize()
sls.push(88)
sls.printStack()
sls.stackSize()
