class Leaderboard:

    def __init__(self):
        self.d = defaultdict(int)

    def addScore(self, playerId, score):
        self.d[playerId] += score    

    def top(self, K):
        heap = [] 
        for x in self.d.values():
            heappush(heap, x)
            if len(heap) > K:
                heappop(heap) # min heap, pop out min
        return sum(heap)
        
    def reset(self, playerId):
        del self.d[playerId]


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
