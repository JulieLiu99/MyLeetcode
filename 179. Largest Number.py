class Solution:

    # Custom comparator + default sort
    # Time O(nlogn)
    # Space O(n)

    num_strings = [str(num) for num in nums]

    def compare(n1, n2):
        if n1 + n2 > n2 + n1:
            return -1 # means n1 should come before n2
        else:
            return 1 # means n1 should come after n1

    num_strings = sorted(num_strings, key=cmp_to_key(compare))

    if num_strings[0] == "0":
        return "0"

    return "".join(num_strings)

#     For each element, check if it needs to be swapped with any other.
#     Compare function checks if the current order of elements gives max value.
    
#     Time O(n^2)
#     Space O(1)

    """
    def compare(self, n1, n2):
        return str(n1) + str(n2) >= str(n2) + str(n1)
    """
    
#     Bubble Sort
#     Bubble Sort repeatedly swaps the adjacent elements if they are in wrong order.

    
    """
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums), 0, -1):
            for j in range(i-1):
                if not self.compare(nums[j], nums[j+1]):
                    nums[j], nums[j+1] = nums[j+1], nums[j]
               # add int() here to avoid "00"
        return str(int("".join(map(str, nums))))
    """
    
    
#     Selection Sort 
#     Repeatedly finds the minimum element (considering ascending order) from unsorted part and putting it at the beginning. 

    """
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)-1, -1, -1):
            max_idx = 0
            for j in range(i+1):
                if not self.compare(nums[j], nums[max_idx]):
                    max_idx = j
            nums[max_idx], nums[i] = nums[i], nums[max_idx]
        return str(int("".join(map(str, nums))))
    
    """
    # Insertion Sort
    # Values from the unsorted part are picked and placed at the correct position in the sorted part.
    
    """
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            pos, cur = i, nums[i]
            while pos > 0 and not self.compare(nums[pos-1], cur):
                nums[pos] = nums[pos-1]     # Move the greater elements one position up 
                pos -= 1                    # to make space for the swapped element
            nums[pos] = cur
        return str(int("".join(map(str, nums))))
    """