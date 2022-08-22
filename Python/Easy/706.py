class MyHashMap:

    def __init__(self):
        self.hash = [None] * 1000001

    def put(self, key: int, value: int) -> None:
        self.hash[key] = value

    def get(self, key: int) -> int:
        if self.hash[key] != None:
            return self.hash[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        self.hash[key] = None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
# [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
