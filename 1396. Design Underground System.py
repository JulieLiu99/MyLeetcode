class UndergroundSystem:
    """
    Two dictionaries
    
    Time O(1)
    Space O(n)
    """

    def __init__(self):
        self.idMap = dict() # (checkin_time, checkin_station)
        self.timeMap = dict() # (count, total_time)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.idMap[id] = (t, stationName)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        checkin_time, checkin_station = self.idMap[id]

        key = (checkin_station, stationName)
        if key not in self.timeMap:
            self.timeMap[key] = [0, 0]
        
        self.timeMap[key][0] += 1
        self.timeMap[key][1] += t - checkin_time

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        count, total_time = self.timeMap[(startStation, endStation)]
        return total_time / count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
