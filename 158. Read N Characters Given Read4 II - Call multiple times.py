# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    """
    The return value is the number of actual characters read
    
    Note: 
    We need to have an __init__(self) to maintain deque
    Because method read(self, buf, n) may be called multiple times
    
    Time O(n): assuming read4 is O(1)
    Space O(n)
    
    """
        
    def __init__(self):
        self.buf = deque()
        
    def read(self, buf: List[str], n: int) -> int:
        
        next_buf = 4 * ['']
        while len(self.buf) < n and read4(next_buf):
            self.buf.extend(next_buf)
            next_buf = 4 * ['']
        buf_ptr = 0
        while self.buf and buf_ptr < n:
            buf[buf_ptr] = self.buf.popleft()
            buf_ptr += 1
        return buf_ptr
