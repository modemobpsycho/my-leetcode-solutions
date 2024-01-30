class StockSpanner:
    def __init__(self) -> None:
        self.stocks: list = []
        self.order: list = []

    def next(self, price: int) -> int:
        if len(self.order) == 0:
            self.order.append(price)
            self.stocks.append((price, 0))
            return 1

        index: int = len(self.order)

        while self.stocks and self.stocks[-1][0] <= price:
            self.stocks.pop()

        if len(self.stocks) == 0:
            res: int = index + 1
        else:
            res = index - self.stocks[-1][1]

        self.order.append(price)
        self.stocks.append((price, index))
        return res
