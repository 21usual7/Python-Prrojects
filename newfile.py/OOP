import random

class StockMarket:
    def __init__(self):
        self.stock_data = {"Meta": 150, "Apple": 200, "Nvidia": 350}

    def display_stock_info(self):
        return self.stock_data

    def buy_stock(self, ticker, amount, balance):
        stock_price = self.stock_data[ticker]
        total_cost = stock_price * amount
        if amount <= 0:
            return "Amount must be greater than zero."
        if balance < total_cost:
            return f"You don't have enough credit to buy {amount} of {ticker}. It costs {total_cost}, but you only have {balance}."
        self.stock_data[ticker] += 10  # Increase stock price
        balance -= total_cost
        return f"Successfully bought {amount} of {ticker} for {total_cost}. Remaining balance: {balance}"

    def sell_stock(self, ticker, amount, balance):
        stock_price = self.stock_data[ticker]
        total_earnings = stock_price * amount
        self.stock_data[ticker] -= 10  # Decrease stock price
        balance += total_earnings
        return f"Successfully sold {amount} of {ticker} for {total_earnings}. New balance: {balance}"


class RandomStrategy:
    def random_strategy(self, stock_market):
        stock_data = stock_market.display_stock_info()
        stock_ticker = random.choice(list(stock_data.keys()))
        action = random.choice(["Buy", "Sell"])
        max_amount = 10  # Limit random purchases/sales to a max of 10 stocks
        random_amount = random.randint(1, max_amount)
        return stock_ticker, action, random_amount


class AnalogyStrategy:
    def analogy_strategy(self, stock_market, stock_ticker):
        stock_data = stock_market.display_stock_info()
        current_price = stock_data[stock_ticker]
        previous_price = current_price - 10  # Example logic to simulate previous price
        if previous_price < current_price:
            return "Buy"
        elif previous_price > current_price:
            return "Sell"
        else:
            return "Hold"


class HypeStrategy:
    def hype_strategy(self, stock_market, stock_ticker):
        stock_data = stock_market.display_stock_info()
        current_price = stock_data[stock_ticker]
        previous_price = current_price + 1  # Example logic

        if previous_price < current_price:
            return "Buy"
        elif previous_price > current_price:
            return "Sell"
        else:
            return "Nothing is Hyping right now 🔥"


class Trader:
    def __init__(self, balance, strategy):
        self.balance = balance
        self.strategy = strategy  # Strategy should be an instance of RandomStrategy, AnalogyStrategy, or HypeStrategy

    def make_trade_random(self, stock_market):
        stock_ticker, action, random_amount = self.strategy.random_strategy(stock_market)
        if action == "Buy":
            result = stock_market.buy_stock(stock_ticker, random_amount, self.balance)
        elif action == "Sell":
            result = stock_market.sell_stock(stock_ticker, random_amount, self.balance)
        else:
            result = "No action taken."
        # Update balance from result
        try:
            self.balance = int(result.split("Remaining balance: ")[-1])  # Extract updated balance
        except ValueError:
            pass
        return result

    def make_analogy_trade(self, stock_market, stock_ticker):
        action = self.strategy.analogy_strategy(stock_market, stock_ticker)
        amount = 1  # Define a default amount for analogy strategy
        if action == "Buy":
            return stock_market.buy_stock(stock_ticker, amount, self.balance)
        elif action == "Sell":
            return stock_market.sell_stock(stock_ticker, amount, self.balance)
        else:
            return "No action taken."

    def make_hype_trade(self, stock_market, stock_ticker):
        action = self.strategy.hype_strategy(stock_market, stock_ticker)
        amount = 1  # Define a default amount for hype strategy
        if action == "Buy":
            return stock_market.buy_stock(stock_ticker, amount, self.balance)
        elif action == "Sell":
            return stock_market.sell_stock(stock_ticker, amount, self.balance)
        else:
            return "No Hyping right now."


class StockInfo:
    def __init__(self, stock_market):
        self.stock_data = stock_market.display_stock_info()
        self.price_history = {ticker: [price] for ticker, price in self.stock_data.items()}

    def update_price(self, ticker, new_price):
        if ticker in self.price_history:
            self.price_history[ticker].append(new_price)
        else:
            self.price_history[ticker] = [new_price]

    def get_price_history(self, ticker):
        return self.price_history.get(ticker, [])


class Simulation:
    def __init__(self, stock_market, traders, stock_info, rounds=10):
        self.stock_market = stock_market
        self.traders = traders
        self.stock_info = stock_info
        self.rounds = rounds

    def run(self):
        for round_number in range(1, self.rounds + 1):
            print(f"=== Round {round_number} ===")
            for trader in self.traders:
                if isinstance(trader.strategy, RandomStrategy):
                    result = trader.make_trade_random(self.stock_market)
                elif isinstance(trader.strategy, AnalogyStrategy):
                    stock_ticker = random.choice(list(self.stock_market.display_stock_info().keys()))
                    result = trader.make_analogy_trade(self.stock_market, stock_ticker)
                elif isinstance(trader.strategy, HypeStrategy):
                    stock_ticker = random.choice(list(self.stock_market.display_stock_info().keys()))
                    result = trader.make_hype_trade(self.stock_market, stock_ticker)
                print(result)

            for ticker, current_price in self.stock_market.display_stock_info().items():
                self.stock_info.update_price(ticker, current_price)

        print("=== Simulation Complete ===")
        for ticker in self.stock_info.price_history:
            print(f"Price history for {ticker}: {self.stock_info.get_price_history(ticker)}")


# Example usage
stock_market = StockMarket()
stock_info = StockInfo(stock_market)
random_strategy = RandomStrategy()
analogy_strategy = AnalogyStrategy()
hype_strategy = HypeStrategy()

trader_random = Trader(balance=1000, strategy=random_strategy)
trader_analogy = Trader(balance=1500, strategy=analogy_strategy)
trader_hype = Trader(balance=2000, strategy=hype_strategy)

simulation = Simulation(
    stock_market=stock_market,
    traders=[trader_random, trader_analogy, trader_hype],
    stock_info=stock_info,
    rounds=10
)

simulation.run()