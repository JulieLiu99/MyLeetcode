class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tree = {}
        

    def addWord(self, word: str) -> None:
        t = self.tree

        # Creating a nested dictionary from word's characters
        for c in word:
            if c not in t:
                t[c] = {}
            t = t[c]
        
        # Add end of word mark to the dictionary of current node
        t['#'] = '#'
        

    def search(self, word: str) -> bool:
        return self.searchNode(self.tree, word)

    def searchNode(self, node, word: str) -> bool:
        """
        Time O(L) where L is word length.
        Worst case Time O(26^L), if word has '.' on each character.
        Space O(h*26) where h is the maximum height of the tree.
        """
        for i, c in enumerate(word):
            if c == '.':
                # Search for any sub-string starting with current character
                for w in node:
                    if w != '#':
                        if self.searchNode(node[w], word[i+1:]):
                            return True
                return False
            
            if c not in node:
                return False
            
            node = node[c] # found, move to current character node
        
        # IF any word found there should be 
        # end of word mark in the dictionary of current node
        return '#' in node


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
