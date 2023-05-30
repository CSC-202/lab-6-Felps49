class Node:
    value: any
    next: any

    def __init__(self, value, next):
        self.value = value
        self.next = next


class List:
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


def initialize() -> List:
    raise NotImplementedError("List.initialize() not defined")


def isEmpty(data: List) -> bool:
    raise NotImplementedError("List.isEmpty() not defined")


def addAtIndex(data: List, index: int, value: int) -> List:
    if (data is None):
        return Node(value)
    if (index == 1):
        newnode = Node(data)
        newnode.next = data
        data = newnode
        return data 
    else:
        data.next = addAtIndex(data.next, index -1, value)
    return data
    # raise NotImplementedError("List.addAtIndex() not defined")


def removeAtIndex(data: List, index: int) -> tuple[Node, List]:
    def helper(v: Node, index: int, i: int):
        if i + 1 == index:
            target: Node = v.next
            v.next = target.next
            return target
        elif i > index:
            raise IndexError('oops')
        else:
            return helper(v.next, index, i + 1)
    if isEmpty(data):
        return None
    elif index < 0 or index >= len(data):
        raise IndexError('oops')
    else:
        return helper(data.first, index, i = 0)
    # raise NotImplementedError("List.removeAtIndex() not defined")


def addToFront(data: List, value: int) -> List:
    if (data == None):
        return None
    else:
        data.next = addToFront(data.next, value)
    return data
    # raise NotImplementedError("List.addToFront() not defined")


def addToBack(data: List, value: int) -> List:
    if (data == None):
        new = Node(value)
        return new
    if data.next == None:
        new = Node(value)
        addToBack(data.next, value)
    return data
    #raise NotImplementedError("List.addToBack() not defined")


def getElementAtIndex(data: List, index: int) -> Node:
    def helper(v: Node, index: int, i: int):
        if i == index:
            return v
        elif i > index:
            raise IndexError('oops')
        else:
            return helper(v.next, index, i + 1)
    if isEmpty(data):
        return None
    elif index < 0 or index >= len(data):
        raise IndexError('oops')
    else:
        return helper(data.first, index, i = 0)
    # raise NotImplementedError("List.getElementAtIndex() not defined")


def clear(data: List) -> List:
    raise NotImplementedError("List.clear() not defined")
