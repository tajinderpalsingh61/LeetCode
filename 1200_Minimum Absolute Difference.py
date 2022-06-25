class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr = sorted(arr)
        min_val = 100000000000
        out_list = []
        
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i] < min_val:
                out_list = [[arr[i], arr[i+1]]]
                min_val = arr[i+1]-arr[i]
            elif arr[i+1]-arr[i] == min_val:
                out_list.append([arr[i], arr[i+1]])
            else:
                pass
            
            
        return out_list