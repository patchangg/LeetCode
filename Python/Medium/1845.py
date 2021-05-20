import heapq

class SeatManager:

    def __init__(self, n):
        self.unSeats = [i for i in range(1,n+1)]

    def reserve(self):
        return heapq.heappop(self.unSeats)

    def unreserve(self, seatNumber):
        heapq.heappush(self.unSeats,seatNumber)


# Heaps are a special tree structure where parents are less than the child node
# so using heaps will make sure that the list is always sorted
# which allows us to easily pop and append seats into the list 
# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
