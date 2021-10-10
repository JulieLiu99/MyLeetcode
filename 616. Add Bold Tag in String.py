class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        
        # create trie tree
        trie_root = {}
        for word in words:
            cur = trie_root
            for c in word:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
            cur["#"] = 1

        # interval merge
        intervals = []
        def add_interval(interval):
            if intervals and intervals[-1][1] >= interval[0]:
                intervals[-1][1] = max(intervals[-1][1], interval[1])
            else:
                intervals.append(interval)

        # match and add to interval
        n = len(s)
        for i in range(n):
            cur = trie_root
            for j in range(i, n):
                if s[j] not in cur:
                    break
                cur = cur[s[j]]
                if "#" in cur:
                    add_interval([i, j+1])

        # concatenate result
        res = ""
        prev = 0
        for start, end in intervals:
            res += s[prev:start] + '<b>' + s[start:end] + "</b>"
            prev = end
        return res + s[prev:]
