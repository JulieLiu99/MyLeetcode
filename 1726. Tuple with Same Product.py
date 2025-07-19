class Solution(object):
    def tupleSameProduct(self, nums):
        """
        Hash map to count pairs with same product

        Math for combinatories and permutations to count tuples

        Time O(n^2)
        Space O(n^2)
        """
        n = len(nums)

        product_count = {} # pair product value: count
        solution = 0

        for i in range(n):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]
                if product in product_count:
                    product_count[product] += 1
                else:
                    product_count[product] = 1

        for count in product_count.values():
            # choose two pairs from all pairs
            pairs_of_equal_product = count * (count - 1) // 2

            # two pairs can form 8 tuples
            solution += 8 * pairs_of_equal_product

        return solution
