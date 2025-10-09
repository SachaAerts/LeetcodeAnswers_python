class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        step = 1
        for index in range(1, len(nums)):
            if self.isNumberAccepted(nums, step, index):
                nums[step] = nums[index]
                step += 1
        return step

    def isNumberAccepted(self, nums, step, index):
        if step == 0:
            return True
        return nums[step - 1] != nums[index]

