# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        """
        Recursion
        
        For each nested list, add 1 to depth, and get its recursion return 
        For each integer in the current nested list, its value is ele.getInteger() * depth
        
        Time O(n)
        Space O(n)
        
        """
        def get_weighted_sum(input_list, depth):
            
            result = 0
            for ele in input_list:
                if ele.isInteger():
                    result += ele.getInteger() * depth
                else:
                    result += get_weighted_sum(ele.getList(), depth+1)
            
            return result
        
        return get_weighted_sum(nestedList, 1) # whatever intergeer in the first nest has depth 1
