import requests
import pandas as pd
from datetime import datetime

def fetch_market_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 50,
        "page": 1,
        "sparkline": False,
        "price_change_percentage": "30d"
    }
    response = requests.get(url, params=params)
    data = response.json()

    df = pd.DataFrame(data)
    # Optional: print column names to debug
    print("Columns received:", df.columns.tolist())

    df = df[[
        "id", "symbol", "name", "current_price",
        "market_cap", "total_volume",
        "price_change_percentage_30d_in_currency"
    ]]
    df["fetched_at"] = datetime.utcnow()
    df.to_csv("data/crypto_snapshot.csv", index=False)

if __name__ == "__main__":
    fetch_market_data()
