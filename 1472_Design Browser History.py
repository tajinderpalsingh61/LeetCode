class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = []
        self.history.append(homepage)
        self.curr = 0
        
    def visit(self, url: str) -> None:
        self.history = self.history[0:self.curr+1]
        self.history.append(url)
        self.curr+=1
        #print("visit", self.history, self.curr)
        return None
        
    def back(self, steps: int) -> str:        
        self.curr = max(0, self.curr-steps)
        #print("back", self.history, self.curr)
        return self.history[self.curr]
    
    def forward(self, steps: int) -> str:        
        self.curr = min(len(self.history)-1, self.curr+steps)
        #print("fwd", self.history, self.curr)
        return self.history[self.curr]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)