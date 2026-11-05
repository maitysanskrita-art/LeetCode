class AllOne:

    def __init__(self):
        self.count = {}
        self.buckets = {}

    def inc(self, key: str) -> None:
        c = self.count.get(key, 0)
        self.count[key] = c + 1
        self.buckets.setdefault(c + 1, set()).add(key)

        if c > 0:
            self.buckets[c].remove(key)
            if not self.buckets[c]:
                del self.buckets[c]

    def dec(self, key: str) -> None:
        c = self.count[key]
        self.buckets[c].remove(key)

        if c == 1:
            del self.count[key]
        else:
            self.count[key] = c - 1
            self.buckets.setdefault(c - 1, set()).add(key)

        if not self.buckets[c]:
            del self.buckets[c]

    def getMaxKey(self) -> str:
        if not self.count:
            return ""
        return next(iter(self.buckets[max(self.buckets)]))

    def getMinKey(self) -> str:
        if not self.count:
            return ""
        return next(iter(self.buckets[min(self.buckets)]))