class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        """
        Get count of alphabetic letters for each word

        Time O(n * l1 + m * l2): l1/2 is avg len of words in words1/2
        Space O(1) excluding ans
        """
        def count(word):
            count = [0] * 26
            for letter in word:
                count[ord(letter) - ord("a")] += 1
            return count

        # Count of each alphabetic letter required in a universial word
        count_words2 = [0] * 26
        for word2 in words2:
            count_word2 = count(word2)
            for i, c in enumerate(count_word2):
                count_words2[i] = max(count_words2[i], c)

        ans = []
        for word1 in words1:
            if all(c1 >= c2 for c1, c2 in zip(count(word1), count_words2)):
                ans.append(word1)
        return ans