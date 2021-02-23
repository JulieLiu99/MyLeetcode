class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        Time O(n) where n is lenght of word
        Space O(n) worst case have to add all chars in a word
        """
        node = self.root
        for char in word:
            if char in node.keys():
                node = node[char]   # go down to child
            else:
                node[char] = {}     # insert char 
                node = node[char]   # go down to leaf
        node['is_word'] = True      # mark leaf
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        Time O(n) 
        Space O(1) no extra storage
        """
        node = self.root
        for char in word:
            if char in node.keys():
                node = node[char]
            else:
                return False
        
        if 'is_word' in node.keys():
            return True
        else:
            return False
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        Time O(n)
        Space O(1)
        """
        node = self.root
        for char in prefix:
            if char in node.keys():
                node = node[char]
            else:
                return False
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
