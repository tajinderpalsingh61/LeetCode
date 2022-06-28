class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        
        for i in range(len(nums)):
            pen = target-nums[i]
            if pen in d.keys():
                return [d[pen], i]
            else:
                d[nums[i]] = i