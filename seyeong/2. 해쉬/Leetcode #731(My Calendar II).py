class MyCalendarTwo:

    def __init__(self):
        self.cal = []
        self.overrap = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.overrap:
            ms = max(start, s)
            me = min(end, e)
            if ms < me:
                return False
            
        for s, e in self.cal:
            ms = max(start, s)
            me = min(end, e)
            if ms < me:
                self.overrap.append([ms,me])
        
        
        self.cal.append([start, end])
        
        # print(self.cal, self.overrap)
        return True
# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)