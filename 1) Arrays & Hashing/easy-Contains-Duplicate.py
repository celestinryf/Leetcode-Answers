class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Hash Set

        # length 1

        numsSet = set(nums)
        if len(numsSet) == len(nums):
            return False
        else:
            return True

        # length 2

        return len(set(nums)) < len(nums)

        # 2

        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

        # sorting

        nums.sort() # sorting method
        for i in range(1, len(nums)): # start at 1 to avoid out of bounds
            if nums[i] == nums[i - 1]: # check current and previous indices
                return True
        return False