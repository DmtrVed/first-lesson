class Stack:
    def __init__(self):
        self._items = []

    def is_empty(self):
        if len(self._items) == 0:
            return True
        else:
            return False

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if len(self._items) == 0:
            raise IndexError
        return self._items.pop()

    def peek(self):
        if len(self._items) == 0:
            raise IndexError
        return self._items[-1]

    def size(self):
        return len(self._items)