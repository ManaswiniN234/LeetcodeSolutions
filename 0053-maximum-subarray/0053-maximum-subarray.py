class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cmax = nums[0]
        tmax = nums[0]

        for i in range(1, len(nums)):
            cmax = max(nums[i], cmax + nums[i])
            tmax = max(cmax, tmax)
        return tmax


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna