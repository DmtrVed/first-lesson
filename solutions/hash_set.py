class HashSet:
    def __init__(self, size = 10):
        self.size = size
        self.buckets = [[] for _ in range(size)]
        self.count = 0

    def _hash(self, value):
        return hash(value) % self.size

    def add(self, value):
        bucket_ind = self._hash(value)
        bucket = self.buckets[bucket_ind]
        if value not in bucket:
            bucket.append(value)
            self.count += 1

    def remove(self, value):
        bucket_ind = self._hash(value)
        bucket = self.buckets[bucket_ind]
        if value in bucket:
            bucket.remove(value)
            self.count -= 1

    def contains(self, value):
        bucket_ind = self._hash(value)
        return value in self.buckets[bucket_ind]

    def __len__(self):
        return self.count