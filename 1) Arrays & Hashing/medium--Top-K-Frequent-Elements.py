class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # optimal solution

        # create a hash to have the keys, and values
        count = {}
        # create an array of empty arrays the length of the input
        freq = [[] for i in range(len(nums) + 1)]

        # for each value in the input add it to the array and count its occurences
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        # for each value and num of occurences, append to frequencies
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        # for the num of frequencies, append thehighest frequencies to the result arr
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                # when we have populated the num of values as k we are done
                if len(res) == k:
                    return res


        # My solution

        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
