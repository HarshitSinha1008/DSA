class Solution(object):
    def majorityElement(self, nums):

        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1
       
        most_frequent = max(count, key=count.get)
        return most_frequent