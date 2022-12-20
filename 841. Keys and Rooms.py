class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        """
        Turn this to a graph question: rooms are nodes and keys are edges
        Keep track of which rooms we have visited to avoid visiting the same room more than once.
        Time O(M+N)
        Space O(N)
        """
        visited = set()
        
        def dfs(room):
            if room not in visited: 
                visited.add(room)
                for key in rooms[room]:
                    dfs(key) # visit neighboring rooms

        dfs(0) # start from the first room
        
        return len(visited) == len(rooms) # make sure we've visited all rooms
