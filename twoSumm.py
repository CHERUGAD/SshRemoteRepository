class Solutions():
    def twoSum(self, nums, target):
        hashmap = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[num] = i
sol = Solutions()
print(sol.twoSum([2, 7, 11, 15], 9)) # [0, 1]
print(sol.twoSum([3, 2, 4], 6)) # [1, 2]
print(sol.twoSum([3, 3], 6)) # [0, 1]


# The above code defines a class `Solutions` with a method `twoSum` that takes a list of integers `nums` and an integer `target`.
# The method finds two indices in `nums` such that the numbers at those indices add up to `target`. It uses a dictionary `hashmap` to store the numbers it has seen so far and their indices
# The code then creates an instance of the `Solutions` class and calls the `twoSum
#` method with different inputs, printing the results.
# The expected output for the three test cases is:
# [0, 1], [1, 2], and [0, 1] respectively.
# The first test case finds the indices of 2 and 7 in the list [2, 7, 11, 15] that add up to 9.
# The second test case finds the indices of 2 and 4 in the list [3, 2, 4] that add up to 6.
# The third test case finds the indices of 3 and 3 in the list [3, 3] that add up to 6.
# The code is a simple implementation of the two-sum problem using a hash map to achieve O(n) time complexity.
# The code is well-structured and easy to understand, with clear variable names and a concise implementation

#Another way to solve the two-sum problem is to use a brute-force approach, which has a time complexity of O(n^2).
# This approach involves using two nested loops to check all pairs of numbers in the list to see if they add up to the target.Here is an example of how this could be implemented in Python:
class Solutions():
    def twoSums(self, nums,target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
sol = Solutions()
print(sol.twoSums([2, 7, 11, 15], 9)) # [0, 1]
print(sol.twoSums([3, 2, 4], 6)) # [1, 2]   
print(sol.twoSums([3, 3], 6)) # [0, 1]
# The brute-force approach is less efficient than the hash map approach, especially for larger lists, as it has a time complexity of O(n^2).    
# However, it is a straightforward solution that is easy to understand and implement.
# The expected output for the three test cases is the same as before:
# [0, 1], [1, 2], and [0, 1] respectively.
# The first test case finds the indices of 2 and 7 in the list [2, 7, 11, 15] that add up to 9. 
# The second test case finds the indices of 2 and 4 in the list [3, 2, 4] that add up to 6.
# The third test case finds the indices of 3 and 3 in the list [3, 3] that add up to 6.
# The code is a simple implementation of the two-sum problem using a brute-force approach.