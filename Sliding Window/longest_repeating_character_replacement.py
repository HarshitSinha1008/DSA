class Solution(object):
    def characterReplacement(self, s, k):

        left = 0
        count = {}
        max_length = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1 
            maxFreq = max(count.values())

            while ((right - left + 1) - maxFreq) > k:
                count[s[left]] -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)
        
        return max_length


        