import nasdaqdatalink

data = nasdaqdatalink.get("MULTPL/SP500_DIV_YIELD_MONTH")

data.plot(title="S&P 500 dividend yield (12 month dividend per share)/price")
