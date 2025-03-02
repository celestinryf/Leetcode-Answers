class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        ### WITH A SET

        seen = set()
        for num in nums:
            if num in seen:
                seen.remove(num)
            else:
                seen.add(num)
        return list(seen)[0]


        ### WITH A SORT

        class Solution2:
            def singleNumber(self, nums: List[int]) -> int:
                nums.sort()
                i = 0
                while i < len(nums) - 1:
                    if nums[i] == nums[i + 1]:
                        i += 2
                    else:
                        return nums[i]
                return nums[i]


        ### WITH BIT MANIPULATION

        class Solution:
            def singleNumber(self, nums: List[int]) -> int:
                res = 0
                for num in nums:
                    res = num ^ res   ## XOR OPERATOR, CANCELS AND OPERATIONS REMOVING DUPLICATE PAIRS
                return res

