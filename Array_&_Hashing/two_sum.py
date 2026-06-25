class Solution(object):
    def twoSum(self, nums, target):

        nums_index = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in nums_index:
                return [nums_index[diff], i]

            nums_index[num] = i