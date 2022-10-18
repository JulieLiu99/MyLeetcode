class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        """
        Time O(n^2)
        Space O(n)
        
        """
        closer_friends = {} # person: a list of people they are closer to than the person they are paired with
        
        for a, b in pairs:
            closer_friends[a] = preferences[a][:preferences[a].index(b)]
            closer_friends[b] = preferences[b][:preferences[b].index(a)]
            
        res = 0
        for person, friends in closer_friends.items():
            for friend in friends:
                if person in closer_friends[friend]: # matual relationship but not together :(
                    res += 1
                    break
        return res
