class BrowserHistory:

    def __init__(self, homepage: str):
        #pointer to homepage, same as index of homepage
        self.curr = 0
        self.history = [homepage]
        

    def visit(self, url: str) -> None:
        if len(self.history) >= self.curr + 2:
            self.history[self.curr + 1] = url
            self.curr += 1
        else:
            self.history.append(url)
            self.curr += 1

        for i in range(len(self.history)-1, self.curr, -1):
            self.history.pop(i)


    def back(self, steps: int) -> str:
        self.curr = max(self.curr - steps, 0)
        print(self.curr)
        print(self.history)
        return self.history[self.curr]

    def forward(self, steps: int) -> str:
        self.curr = min(self.curr + steps, len(self.history)-1)
        return self.history[self.curr]

        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)