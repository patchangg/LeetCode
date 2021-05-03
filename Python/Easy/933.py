class RecentCounter:

    def __init__(self):
        self.pings = []

    def ping(self,t):
        self.pings.append(t)
        while self.pings[0] < (t - 3000):
            self.pings.pop(0)
        return len(self.pings)


# ["RecentCounter", "ping", "ping", "ping", "ping"]
# [[], [1], [100], [3001], [3002]]
# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter()
param_1 = obj.ping(1)
param_1 = obj.ping(100)
param_1 = obj.ping(3001)
param_1 = obj.ping(3002)
