import cryptocompare
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
from datetime import datetime
import random

plt.style.use("seaborn")

cryptocurrencies = ["BTC", "ETH", "DOGE", "SHIB", "BCH", "ETC", "BNB", "USDT", "SOL", "ADA"]
random_crypto = random.choice(cryptocurrencies)

x_values = []
y_values = []

def getRealTimeData(crypto: str) -> int:
    return cryptocompare.get_price(crypto, "USD")[crypto]["USD"]

def getCryptoName(cryptocurrency: str) -> str:
    return cryptocompare.get_coin_list()[cryptocurrency]["FullName"]

def graphData(i) -> None:

    x_values.append(datetime.now())
    y_values.append(getRealTimeData(random_crypto))

    plt.cla()

    plt.title(getCryptoName(random_crypto))

    plt.xlabel("Date")
    plt.ylabel("Price (USD$)")

    plt.plot_date(x_values, y_values, linestyle = "solid", ms = 0)
    plt.tight_layout()

if __name__ == "__main__":

    animation = FuncAnimation(plt.gcf(), graphData, interval = 1000)
    plt.show()