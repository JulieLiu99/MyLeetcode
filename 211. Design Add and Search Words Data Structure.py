class WordDictionary:
    """
    word may contain dots '.' where dots can be matched with any letter
    
    Brute Force: Store every word. For every search, check all words stored.
    
    Trie (Prefix Tree) + DFS for '.'
    
    Create hashmaps where one char leads to the next char in the same word
    
            /   |   \
           b    d    m
          /     |     \
         a      a      a
        /       |       \
       d        d        d
      END      END      END
          
    Why need END mark for last node: 
        if search word is "ba", all of its chars can be matched, 
        but it does not match the complete word.
     
    DFS search for a word:
    
    If current char matches with a record in curr.children, move to next char    
    If current char is ., it automatically matches with any char, move to next char in all curr.children
    
    Time O(L), worst case all '.' O(N)
    Space O(N)
    
    """
    """

    def __init__(self):
        self.children = {} # char: next node representing the next char within the word
        self.isEnd = False

    def addWord(self, word: str) -> None:
        curr = self  # root
        for c in word:
            if c not in curr.children:
                curr.children[c] = WordDictionary()
            curr = curr.children[c]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        curr = self  # root
        for i in range(len(word)):
            c = word[i]
            if c != ".":
                if c not in curr.children:
                    return False
                else:
                    curr = curr.children[c]
            else:
                # period case
                for _, child_node in curr.children.items():
                    if child_node.search(word[i + 1:]):
                        return True
                return False
        return curr.isEnd
    """
        
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
        Worst case Time O(N), if word has '.' on each character.
        Space O(N) where h is the maximum height of the tree.
        
        """
        for i, c in enumerate(word):
            if c == '.':
                # Search for any sub-string starting with current character
                for cur_c in node:
                    if cur_c != '#':
                        if self.searchNode(node[cur_c], word[i+1:]):
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