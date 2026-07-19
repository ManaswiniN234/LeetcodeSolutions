class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}
        for i, num in enumerate(nums):
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        ans = 0
        for k, v in freq.items():
            if v > (len(nums)//2):
                ans = k
        return ans

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna