class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
                
        # Dict Implementation
        """
        dict_freq = {}
        for x in nums:
            if x in dict_freq:
                dict_freq[x] +=1
            else:
                dict_freq[x] =0
                
                
        dict_freq = {k:v for k, v in sorted(dict_freq.items(), key=lambda x: x[1], reverse=True)}
        out = []
        i = 1
        for x in dict_freq.keys():
            out.append(x)
            if i == k:
                return out
            
            i+=1
            
        """
        
        #heap Implementation
        """
        from collections import Counter
        dict_freq = Counter(nums)
        return heapq.nlargest(k, dict_freq.keys(), key=dict_freq.get) 
        """
        
        #Quick select implementation
        from collections import Counter
        counter = dict(Counter(nums))
        unique_elements = list(counter.keys())
        
        
        out = []
        k = len(counter) - k
        l, r = 0, len(unique_elements)-1
        while True:
            p = l
            pivot_index = r
            for i in range(l, r):
                if counter[unique_elements[i]] <=  counter[unique_elements[pivot_index]]:
                    unique_elements[i], unique_elements[p] = unique_elements[p], unique_elements[i]
                    p+=1
                    
            unique_elements[r], unique_elements[p] = unique_elements[p], unique_elements[r]
            
            if p > k:
                l, r = 0, p-1
            elif p < k: 
                l, r = p+1, r
            else:
                return unique_elements[k:]
