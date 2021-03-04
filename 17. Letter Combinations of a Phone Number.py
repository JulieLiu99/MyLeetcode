class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Time O(n 3^n): loop through digits + for each digit loop through ~3 letters
        Space O(n)
        """
        phone = {
            '1': '',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
            '0': ' '}
        
        all_combo = [''] if digits else []
        
        for digit in digits:           
            current_combo = []     
            
            for letter in phone[digit]:
                # append new letter to each of the orignal combo
                for combo in all_combo:
                    current_combo.append(combo + letter) 
            # update orignal combos
            all_combo = current_combo
            
        return all_combo
