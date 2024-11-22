class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Optimal solution

        prevMap = {}  # val -> index

        # enumerate iterates over the array providing index and value at each location
        # i representing index, n representing value
        for i, n in enumerate(nums):
            diff = target - n
            # if this diff is in the map, take the index
            if diff in prevMap:
                return [prevMap[diff], i]
            # populate the map with the array
            prevMap[n] = i


        # My solution

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []