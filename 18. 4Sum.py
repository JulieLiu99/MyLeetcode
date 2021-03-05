class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        """
        Recursion to reduce the N-sum to 2-sum
        Time O(n^3), k-2 loops over n elements, twoSum is O(n)
        Space O(n) for recursion
        """
        
        def findNsum(l, r, target, N, result, results):

            # early termination
            if r-l+1 < N or N < 2 or target < nums[l]*N or target > nums[r]*N: 
                return

            # two pointers solve sorted 2-sum problem
            if N == 2: 
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1

            # recursively reduce N
            else: 
                for i in range(l, r+1):
                    if i == l or (i > l and nums[i-1] != nums[i]):
                        findNsum(i+1, r, target-nums[i], N-1, result+[nums[i]], results)
        
        nums.sort()
        results = []
        findNsum(0, len(nums)-1, target, 4, [], results)
        return results
    
    """

        # Concept - Use a hashmap to store the pairs of sum
        # If find their remaining sum, append into result
        # Time O(n^3)
        # Space O(n^2)

        hashmap = {}    # Store the sum of two numbers and their indexes
        result = set()  # To avoid duplicates, we use set 
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                
                remaining = target - (nums[i] + nums[j])

                if remaining in hashmap:
                    for index_pair in hashmap[remaining]:
                        x, y = index_pair[0], index_pair[1]
                        
                        # check all 4 indexes are different
                        if (i!=x and i!=y) and (j!=x and j!=y):                
                            temp = [nums[i],nums[j],nums[x],nums[y]]
                            temp.sort()
                            result.add(tuple(temp))
                            
                # add the sum and their indexes to hashmap 
                if nums[i] + nums[j] in hashmap:
                    hashmap[nums[i] + nums[j]].append([i, j])
                else:
                    hashmap[nums[i] + nums[j]] = [[i, j]]
                
        return list(result)
    """
