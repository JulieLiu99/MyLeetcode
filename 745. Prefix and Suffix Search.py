import collections
Trie = lambda: collections.defaultdict(Trie)
"""
A lambda function is an anonymous (without name) function, equivalent to (other than name):
def tree():
    return collectsions.defaultdict(tree)
"""

class WordFilter:
    
    """
    Approach #3: Trie of Suffix Wrapped Words

    Insert suffix, followed by '#', followed by the word, all into the trie.
    
    e.g. "apple"
    insert into trie:
            apple#apple
            pple#apple
            ple#apple
            le#apple
            e#apple
            #apple
    For prefix="ap", suffix ="le", find it by querying for le#ap.
    
    Space O(N K^2), where N is number of words, K is max length of a word
    Time O(N K^2 + Q K), where Q is number of queries
    
    """

    def __init__(self, words: List[str]):
        self.trie = Trie()
        
        for weight, word in enumerate(words):
            for i in range(len(word)+1):
                node = self.trie
                node['weight'] = weight
                word_to_insert = word[i:]+'#'+word
                for c in word_to_insert:
                    node = node[c]
                    node['weight'] = weight
        

    def f(self, prefix: str, suffix: str) -> int:
        node = self.trie
        for c in suffix + '#' + prefix:
            if c not in node: return -1
            node = node[c]
        return node['weight']


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
