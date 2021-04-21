class OrderedStream:

    def __init__(self, n):
        self.stream = [""]*n # Make list size of n that is empty
        self.ptr = 0 # pointer starts at 0

    def insert(self, idKey, value):
        self.stream[idKey-1] = value # idKey is 1 space ahead

        if self.ptr == (idKey - 1):
            index = self.ptr
            while index <= len(self.stream) and self.stream[index] != "":
                index += 1 # move index along until empty is returned
            self.ptr = index # move pointer to index
            return self.stream[idKey-1:index] # return chunk
        return [] # return empty list if chunk is not in order

        # if self.stream[self.ptr]:
        #     st = []
        #     while self.stream[self.ptr]:
        #         st.append(self.stream[self.ptr])
        #         self.ptr += 1
        #         if self.ptr >= self.limit:
        #             break
        #     return st
# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
# ["OrderedStream", "insert", "insert", "insert", "insert", "insert"]
# [[5], [3, "ccccc"], [1, "aaaaa"], [2, "bbbbb"], [5, "eeeee"], [4, "ddddd"]]
