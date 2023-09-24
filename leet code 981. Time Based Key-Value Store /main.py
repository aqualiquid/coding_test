class TimeMap:

    def __init__(self):
        self.key_store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.key_store:
            self.key_store[key] = [value, timestamp]
            # values = ["foo", 3]

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.key_store.get(key, [])
        l, r = 0, len(values) - 1
        while l <= r:
            mid = (l + r) // 2
            if values[mid][1] <= timestamp:
                # values = [(1, "bar"), (4, "bar2")]
                res = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res

    def get(self, key: str, timestamp: int) -> str:
        # return: largest timesatamp among the key_store
        res = ""
        values = self.key_store.get(key, [])
        l, r = 0, len(values) - 1
        while l <= r:
            mid = (l + r) // 2
            if values[mid][1] <= timestamp:
                # values = [(1, "bar"), (4, "bar2")]
                res = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)