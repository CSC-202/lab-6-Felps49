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
    return List()
    # raise NotImplementedError("List.initialize() not defined")


def isEmpty(data: List) -> bool:
    if data.first is None:
        return True
    else:
        return False
    # raise NotImplementedError("List.isEmpty() not defined")


def addAtIndex(data: List, index: int, value: int) -> List:
    def helper(v: Node, index: int, value: int):
        if index == 1:
            newnode = Node(value, next)
            newnode.next = v.next
            v.next = newnode
        else:
            helper(v.next, index, index - 1) 
    if index == 0:
        newnode = Node(value, next)
        newnode.next = data.first
        data.first = newnode
    elif index < 0 or index >= len(data):
        raise IndexError('oops')
    else:
        helper(data.first, index, value)
    return data

    # if (data is None):
    #     return Node(value)
    # if (index == 1):
    #     newnode = Node(data)
    #     newnode.next = data
    #     data = newnode
    #     return data 
    # else:
    #     data.next = addAtIndex(data.next, index - 1, value)
    # return data
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
    if data.first is None:
        data.first = Node(value, None)
        return data
    else:
        new_node = Node(value, data.first)
        data.first = new_node
        return data
    # if (data == None):
    #     return None
    # else:
    #     data.next = addToFront(data.next, value)
    # return data
    # raise NotImplementedError("List.addToFront() not defined")


def addToBack(data: List, value: int) -> List:
    def helper(v: Node, value: int):
        if v.next is None:
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

    # if (data == None):
    #     new = Node(value)
    #     return new
    # if data.next == None:
    #     new = Node(value)
    #     addToBack(data.next, value)
    # return data
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
    data.first = None
    return data
    # raise NotImplementedError("List.clear() not defined")
