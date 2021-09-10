class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        """
        Math + Hashtable
        
        Store the difference of the consecutive alpabhets of each letter in a dictionarty and that's it!
        defaultdict(<class 'list'>, {})
        defaultdict(<class 'list'>, {'1.1': ['abc']})
        defaultdict(<class 'list'>, {'1.1': ['abc', 'bcd']})
        defaultdict(<class 'list'>, {'1.1': ['abc', 'bcd'], '2.2.1': ['acef']})
        defaultdict(<class 'list'>, {'1.1': ['abc', 'bcd', 'xyz'], '2.2.1': ['acef']})
        defaultdict(<class 'list'>, {'1.1': ['abc', 'bcd', 'xyz'], '2.2.1': ['acef'], '25': ['az']})
        defaultdict(<class 'list'>, {'1.1': ['abc', 'bcd', 'xyz'], '2.2.1': ['acef'], '25': ['az', 'ba']})
        defaultdict(<class 'list'>, {'1.1': ['abc', 'bcd', 'xyz'], '2.2.1': ['acef'], '25': ['az', 'ba'], '': ['a']})

        
        Time O(n) 
        Space O(n) 

        """
        
        d = collections.defaultdict(list)
        
        for s in strings:
            
            pattern = []
            for i in range(len(s)-1):
                pattern.append(str((ord(s[i+1])-ord(s[i]))%26))
                
            # list is unhashable, convert pattern to string
            pattern = '.'.join(pattern) # needs seperation because each gap can be 1 or 2 digits
            d[pattern].append(s)

        return list(d.values())
