class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        ans = []
        n = len(nums)
        if n == 1:
            return nums
        if k > n:
            k = k % n
        for i in range(n - k, n):
            ans.append(nums[i])
        for i in range(0, n - k):
            ans.append(nums[i])
        nums[:] = ans

        


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna