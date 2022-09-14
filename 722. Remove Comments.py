class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        
        res, inBlock = [], False
        new_str = ""
        
        for line in source:
            # if not in block, start new string
            # if in block, append to existing string
            # ["a/*comment", "line", "more_comment*/b"] --> ["ab"]
            if not inBlock: new_str = ""
            i = 0
            n = len(line)
            while i < n:
                if inBlock: 
                    if i + 1 < n and line[i:i+2] == '*/':
                        i += 2
                        inBlock = False
                        continue
                    i += 1
                else:
                    if i + 1 < n and line[i:i+2] == '/*':
                        i += 2
                        inBlock = True
                        continue
                    if i + 1 < n and line[i:i+2] == '//': # entire line is comment
                        break
                    new_str += line[i]
                    i += 1
            if new_str and not inBlock:
                res.append(new_str)
                    
        return res
