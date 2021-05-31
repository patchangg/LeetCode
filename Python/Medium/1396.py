class UndergroundSystem:

    def __init__(self):
        self.customer = {}
        self.stations = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        #if id not in self.customer:
        self.customer[id] = [stationName,t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        combined = self.customer[id][0] + " " + stationName
        if combined in self.stations:
            self.stations[combined][0] += (t - self.customer[id][1])
            self.stations[combined][1] += 1
        else:
            self.stations[combined] = [(t - self.customer[id][1]),1]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        combined = startStation + " " + endStation
        average = (self.stations[combined][0] / self.stations[combined][1])
        return average

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
