class Solution:

    def __init__(self, nums: List[int]):
        self.d = {}
        for i in range(0, len(nums)):
            if nums[i] in self.d:
                self.d[nums[i]].append(i)
            else:
                self.d[nums[i]] = [i]
        

    def pick(self, target: int) -> int:
        ran_indx =  random.randint(0, len(self.d[target])-1)
        return self.d[target][ran_indx]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)