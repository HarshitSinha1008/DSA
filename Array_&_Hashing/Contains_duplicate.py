class Solution(object):
    def containsDuplicate(self, nums):
        
        x = set(nums)
        return len(nums) != len(x)