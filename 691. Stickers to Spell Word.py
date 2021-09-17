class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        """
        BFS
        
        As long as target as not been met, try all stickers in this round
        While trying a sticker, take advantage of all chars the sticker has, get remaining target for next round
        Count the round
        When target has been met by a sticker, stop at that round, and return the count
        
        Time O(len(target) * len(stickers) * len(sticker))
        Space O(len(stickers) ^ len(target))
        
        """
        
        def use_sticker(cur_target, sticker):
            #supply = defaultdict(int)
            #for char in sticker:
            #    supply[char] += 1
            supply = collections.Counter(sticker)
            still_need = []
            for char in cur_target:
                if char in supply:
                    supply[char] -= 1
                    if supply[char] == 0:
                        del supply[char]
                else:
                    still_need.append(char)
            return ''.join(still_need)
            
        q = deque([target])
        visited = set([target])
        count = 1
        
        while q:
            for _ in range(len(q)):
                cur_target = q.popleft()
                for sticker in stickers: # try each sticker, and get remaining target
                    
                    remaining = use_sticker(cur_target, sticker)
                    if not remaining: 
                        return count
                    if remaining in visited: # means the same target has been processed (maybe is still being processed), no need to repeat the work
                        continue
                    visited.add(remaining)
                    q.append(remaining)
                    
            count += 1
        return -1
