class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Hashmap with sorted key
        
        Time O(nmlogm): Looping over strs O(n), Sorting each str O(mlogm) 
        Space O(n)
        
        """
        hashmap = {}
        for st in strs:
            # USE sorted() AND str.join() TO SORT A STRING ALPHABETICALLY:
            # Sort string alphabetically and return list
            # Combine list elements into one string
            key = ''.join(sorted(st))
            if key not in hashmap:
                hashmap[key] = [st]
            else:
                hashmap[key] += [st]
        return list(hashmap.values())
