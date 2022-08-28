class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 0
        
        # Linear Approach
        """
        for i in range(0, len(nums)):
            if i == 0:
                left = True
                right = True if nums[i] > nums[i+1] else False
            elif i == len(nums)-1:
                left = True if nums[i] > nums[i-1] else False
                right = True
            else:
                left = True if nums[i] > nums[i-1] else False
                right = True if nums[i] > nums[i+1] else False
            
            if left and right:
                return i
        """
        
        #Binary Search Approach
        l = 0
        r = len(nums)-1
        while(l<r):
            mid = (l+r)//2
            if l == r:
                return l
            elif nums[mid] > nums[mid+1]:
                r = mid
            else:
                l = mid+1
                
        return l
            
        