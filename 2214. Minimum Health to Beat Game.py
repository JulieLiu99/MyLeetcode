class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        # Greedy
        # We are using armor on the max damage item
        
        # Time O(n)
        # Space O(1)
        
        return sum(damage) - min(max(damage), armor) + 1
        
