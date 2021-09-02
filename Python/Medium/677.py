class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dicts = {}

    def insert(self, key: str, val: int) -> None:
        if key not in self.dicts:
            self.dicts[key] = val
        else:
            self.dicts[key] = val

    def sum(self, prefix: str) -> int:
        output = 0
        for key,value in self.dicts.items():
            if key.startswith(prefix):
                output += value
        return output

# Initiate class with a dict
# Add the key into the dict when insert is called
# Find each key starting with the prefix and add the values and return it when
# sum is called. sum = O(n), O(1) space
# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
