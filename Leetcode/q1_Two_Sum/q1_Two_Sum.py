class Solution:
    def twoSumBruteForce(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            current = nums[i]
            for j in range(1, len(nums)):
                next_val = nums[j]
                if (i!=j) and (current + next_val == target):
                    return [i,j]
    
    def twoSumHashMap(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, curr in enumerate(nums):
            diff = target - curr
            if diff in hashMap:
                return [hashMap[diff], i]
            else:
                hashMap[curr] = i
        return