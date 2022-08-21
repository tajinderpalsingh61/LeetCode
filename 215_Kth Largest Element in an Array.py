class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        """
        # Max Heap Solution
        from heapq import heapify, heappush, heappop, heapreplace        
        heap = []
        heapify(heap)
        
        for x in nums:
            heappush(heap, -1*x)
            
        for i in range(k):
            val = heappop(heap)
                                 
        return -1*val
        """
        
        #Quick Select solution Avg TC: O(n) SC: O(n)
        """
        k = len(nums)-k
        def quick_select(l, r):
            pivot = nums[r]
            p = l
            for i in range(l, r):
                if nums[i]<=pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p+=1
                    
            nums[p], nums[r] = nums[r], nums[p]
            if p > k: return quick_select(0, p-1)
            elif p < k: return quick_select(p+1, r)
            else: return nums[p]
            
        return quick_select(0, len(nums)-1)
        """
        
        # Quick Select Avg TC: O(n) SC: O(1)
        l, r = 0, len(nums)-1
        k = len(nums)-k
        while(True):
            pivot = nums[r]
            p = l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p+=1
                    
            nums[p], nums[r] = nums[r], nums[p]
                            
            if p > k: l,r = 0, p-1
            elif p < k: l,r = p+1, r
            else: return nums[p]
            