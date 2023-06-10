class Node:
    value: any
    next: any

    def __init__(self, value, next):
        self.value = value
        self.next = next


class Queue:
    first: Node
    last: Node

    def __init__(self):
        self.first = None
        self.last = None

    def __len__(self):
        n: int = 0
        current = self.first
        while current != None:
            n += 1
            current = current.next
        return n

    def toPythonList(self):
        result: list = []
        current = self.first
        while current != None:
            result.append(current.value)
            current = current.next
        return result


def initialize() -> Queue:
    return Queue()
    # raise NotImplementedError("Queue.initialize() not defined")


def isEmpty(data: Queue) -> bool:
    return data.first == None
    # raise NotImplementedError("Queue.isEmpty() not defined")


def enqueue(data: Queue, value: int) -> Queue:
    def helper(v: Node, value: int):
        if v.next == None:
            new_node = Node(value, None)
            v.next = new_node
            return data
        else:
            return helper(v.next, value)
        
    if data.first is None:
        new_node = Node(value, None)
        data.first = new_node
        return data
    else:
        return helper(data.first, value)
    # raise NotImplementedError("Queue.enqueue() not defined")


def dequeue(data: Queue) -> tuple[Node, Queue]:
    if isEmpty(data):
        return None, None
    else: 
        target: Node = data.first
        data.first = target.next
        return target, data
    # raise NotImplementedError("Queue.dequeue() not defined")


def peek(data: Queue) -> Node:
    return data.first.value
    # raise NotImplementedError("Queue.peek() not defined")


def clear(data: Queue) -> Queue:
    data.first = None
    return data
    # raise NotImplementedError("Queue.clear() not defined")
