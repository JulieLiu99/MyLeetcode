class Solution(object):
    def spellchecker(self, wordlist, queries):
        """
        Hashmap

        Preprocess wordlist into 3 maps, in priority order:
        - Exact (case-sensitive)
        - Lowercase (case-insensitive)
        - Vowel-masked (case-insensitive, vowels → *)

        For each query, check in that order

        Time: O(W * L + Q * L)
        Space: O(W * L)
        (W = number of words, Q = queries, L = word length)
        """
        exact = set(wordlist)
        lower_map = {}
        vowel_map = {}

        def mask(word):
            # replace vowels with '*'
            res = []
            for c in word.lower():
                if c in 'aeiou':
                    res.append('*')
                else:
                    res.append(c)
            return ''.join(res)

        # build maps in wordlist order (keeps first occurrence)
        for word in wordlist:
            lw = word.lower()
            if lowered not in lower_map:
                lower_map[lw] = word

            masked = mask(word)
            if mw not in vowel_map:
                vowel_map[mw] = word

        ans = []
        for query in queries:
            # 1) exact match
            if query in exact:
                ans.append(query)
                continue

            lq = query.lower()
            # 2) capitalization match
            if lq in lower_map:
                ans.append(lower_map[lq])
                continue

            mq = mask(query)
            # 3) vowel error match
            if mq in vowel_map:
                ans.append(vowel_map[mq])
                continue

            # 4) no match
            ans.append("")

        return ans
