import pandas as pd
import matplotlib.pyplot as plt

def chart_price_change(data):
    top_gainers = data.sort_values(by="price_change_percentage_30d_in_currency", ascending=False).head(10)
    plt.figure(figsize=(10, 6))
    plt.bar(top_gainers["name"], top_gainers["price_change_percentage_30d_in_currency"])
    plt.xticks(rotation=45)
    plt.ylabel("% Change (30d)")
    plt.title("Top 10 Coins by 30d Price Change")
    plt.tight_layout()
    plt.savefig("charts/top_gainers.png")
    return "charts/top_gainers.png"
