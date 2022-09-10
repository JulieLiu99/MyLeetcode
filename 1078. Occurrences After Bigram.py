class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        
        text = text.split()
        next_words = collections.defaultdict(list)
        
        for i in range(len(text)-2):
            phrase = text[i] + text[i+1]
            next_words[phrase].append(text[i+2])
            
        return next_words[first + second]
