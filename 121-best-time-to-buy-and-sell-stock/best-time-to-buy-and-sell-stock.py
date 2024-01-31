class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = sys.maxsize # int 변수값이므로 int의 가장 큰 값을 할당

        # 순서대로 가면서 최소 가격과 최대 이익을 구한다
        for price in prices:
            min_price = min(min_price, price)
            profit = max(price - min_price, profit)

        return profit