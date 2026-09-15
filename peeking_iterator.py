class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self.next_value = iterator.next() if iterator.hasNext() else None

    def peek(self):
        return self.next_value

    def next(self):
        value = self.next_value
        self.next_value = self.iterator.next() if self.iterator.hasNext() else None
        return value

    def hasNext(self):
        return self.next_value is not None