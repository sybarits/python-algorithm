# 한번의 거래로 낼 수 있는 최대 이익을 산출하라.
import sys


class BestTimeToBuyAndSellStock:

    # 난 브루트 포스가 좋다. 그냥 풀면 되니까!
    # 하지만 이런 풀이는 보통 타임아웃이 나는 법이지....
    def bruteForce(self, prices: list[int]) -> int:
        result = [0 for i in range(len(prices))]

        for i, buyPrice in enumerate(prices):
            for sellPrice in prices[i:]:
                if result[i] < sellPrice - buyPrice:
                    result[i] = sellPrice - buyPrice

        return max(result)

    # O(n)으로 푸는것 처럼 보이지만, min, max 연산 자체가 이미 O(n)아닌가?
    def changeMinMax(self, prices: list[int]) -> int:
        profit = 0
        min_price = sys.maxsize

        for price in prices:
            min_price = min(min_price,price)
            profit = max(profit, price - min_price)

        return profit

    # 이게 더 빠른가?
    def minMax(self, prices: list[int]) -> int:
        minPrice = min(prices)
        maxPrice = max(prices[prices.index(minPrice):])
        return maxPrice - minPrice

if __name__ == "__main__":
    bb = BestTimeToBuyAndSellStock()
    print(bb.bruteForce([7, 1, 5, 3, 6, 4]))
    print(bb.changeMinMax([7, 1, 5, 3, 6, 4]))
    print(bb.minMax([7, 1, 5, 3, 6, 4]))
