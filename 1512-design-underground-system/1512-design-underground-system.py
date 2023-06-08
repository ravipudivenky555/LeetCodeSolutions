class UndergroundSystem:
    def __init__(self):
        self.s2e = {}
        self.id2s = {}
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.id2s[id] = (stationName, t)
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.id2s[id]
        stationsKey = (startStation, stationName)
        if stationsKey not in self.s2e:
            self.s2e[stationsKey] = [t - startTime, 1]
        else:
            self.s2e[stationsKey][0] += t - startTime
            self.s2e[stationsKey][1] += 1
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.s2e[(startStation, endStation)][0] / self.s2e[(startStation, endStation)][1]
# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)