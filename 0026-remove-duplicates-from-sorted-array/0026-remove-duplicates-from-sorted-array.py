class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1
        ui = 1
        while(i < len(nums)):
            if nums[i] == nums[i - 1]:
                pass
            else:
                nums[ui] = nums[i]
                ui += 1
            i+=1
        return ui
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna