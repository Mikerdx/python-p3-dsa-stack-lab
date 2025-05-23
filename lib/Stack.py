class Stack:

    def __init__(self, items = [], limit = 100):
        if items is None:
            items = []
        self.items = items[:limit]  
        self.limit = limit

        pass

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if not self.full():
            self.items.append(item)
        pass

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        return None 

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        return None
    
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) >= self.limit

    def search(self, target):
        try:
            index_from_top = self.items[::-1].index(target)
            return index_from_top
        except ValueError:
            return -1
