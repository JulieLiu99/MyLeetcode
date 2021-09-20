class Codec:
    
    """
    Both encode and decode has time complexity O(1)
    Space complexity O(n)
    
    """

    def __init__(self):
        self.id = 0  # create a ID for the shortened URL. Using a number makes conflicts impossible
        self.shorttolong = {}  
    
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        shortURL = str(self.id)  # create a string of id as the shortURL
        self.shorttolong[shortURL] = longUrl  
        self.id += 1  # increment id for the next shortened URL 
        return shortURL  
        
    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.shorttolong[shortUrl] 
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
