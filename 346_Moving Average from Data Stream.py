class MovingAverage:

    """
    def __init__(self, size: int):
        self.size = size
        self.nums = []
        

    def next(self, val: int) -> float:
        self.nums.append(val)
        if len(self.nums) < self.size:
            return sum(self.nums)/len(self.nums)
        else:
            return sum(self.nums[-1*self.size:])/self.size
    """
        
    #Double Ended queue solution 
    def __init__(self, size: int):
        self.size = size
        self.nums = deque()
        self.window_sum = 0
        self.count=0

    def next(self, val: int) -> float:
        if len(self.nums) == self.size:
            tail = self.nums.popleft()
        else:
            tail = 0
        
        self.nums.append(val)
        self.count+=1
        self.window_sum = self.window_sum - tail + val
        return self.window_sum/min(self.count, self.size)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)