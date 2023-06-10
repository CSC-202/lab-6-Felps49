class Node:
    value: any
    next: any

    def __init__(self, value, next):
        self.value = value
        self.next = next


class Stack:
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


def initialize() -> Stack:
    return Stack()
    # raise NotImplementedError("Stack.initialize() not defined")


def isEmpty(data: Stack) -> bool:
    if data.first is None:
        return True
    else:
        return False
    # raise NotImplementedError("Stack.isEmpty() not defined")


def push(data: Stack, value: int) -> Stack:
    if data.first is None:
        data.first = Node(value, None)
        return data
    else:
        new_node = Node(value, data.first)
        data.first = new_node
        return data
    # raise NotImplementedError("Stack.push() not defined")


def pop(data: Stack) -> tuple[Node, Stack]:
    def helper(v:Node):
        if v.next is not None:
            target: Node = v
            v = v.next
            return target.value, data
        else:
            return helper(v.next)
    if isEmpty(data):
        return None
    else:
        return helper(data.first)
   # raise NotImplementedError("Stack.pop() not defined")


def peek(data: Stack) -> Node:
    return data.first.value
    # raise NotImplementedError("Stack.peek() not defined")


def clear(data: Stack) -> Stack:
    data.first == None
    return data
    # raise NotImplementedError("Stack.clear() not defined")
