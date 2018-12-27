class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        diff_list = [target-num for num in nums]
        if target%2 != 0:
            return [[diff_list.index(diff), nums.index(diff)] for diff in diff_list if diff in nums][0]

        if target%2 == 0:
            half = target/2

            if half in nums and (nums.count(half) > 1):
                x = nums.index(half)
                nums[x] = 'abc'
                y = nums.index(half)
                nums[x] = half
                return [x,y]
            elif half in nums and (nums.count(half) == 1):
                return [[diff_list.index(diff), nums.index(diff)] for diff in diff_list if diff in nums and (diff != half)][0]

            elif half not in nums:
                return [[diff_list.index(diff), nums.index(diff)] for diff in diff_list if diff in nums][0]
