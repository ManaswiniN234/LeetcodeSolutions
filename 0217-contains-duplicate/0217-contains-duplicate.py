class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        freq = {}
        for i in range(len(nums)):
            curr = nums[i]
            if curr in freq:
                freq[curr] += 1
            else:
                freq[curr] = 1
        
        for k,v in freq.items():
            if v > 1:
                return True
        return False 
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna