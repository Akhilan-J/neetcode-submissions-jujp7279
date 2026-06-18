class StockSpanner:

    def __init__(self):
        self.vec = []

    def next(self, price: int) -> int:
        self.vec.append(price)
        res = 0
        for x in range(len(self.vec)-1, -1, -1):
            if(self.vec[x] <= price):
                res += 1
            else:
                break
        return res


    vec = []

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)