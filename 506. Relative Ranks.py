class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        """
        Dictionary mapping score to rank
        
        Time O(n)
        Space O(n)
        
        """
        sorted_score = sorted(score, reverse=True) # high to low
        
        score_medal = {}
        for i, s in enumerate(sorted_score):
            if i == 0:
                score_medal[s] = "Gold Medal"
            elif i == 1:
                score_medal[s] = "Silver Medal"
            elif i == 2:
                score_medal[s] = "Bronze Medal"
            else:
                score_medal[s] = str(i + 1) # 4, 5, 6, ...
                
        return [score_medal[s] for s in score]
