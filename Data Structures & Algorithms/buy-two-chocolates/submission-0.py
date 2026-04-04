class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        something = money - (prices[0] + prices[1]) 
        print(something > 0)
        return something if something >= 0  else money