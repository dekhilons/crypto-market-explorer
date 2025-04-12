# 🧠 Crypto & NFT Market Explorer

![LangChain](https://img.shields.io/badge/langchain-0.2+-blue)
![Streamlit](https://img.shields.io/badge/built%20with-Streamlit-orange)
![Python](https://img.shields.io/badge/python-3.10+-blue)
![Status](https://img.shields.io/badge/status-in--progress-yellow)

> A smart Streamlit-powered dashboard + LangChain agent that lets you query, visualize, and analyze real-time crypto and NFT data using natural language.

---

## 🚀 Features

- 🧩 LangChain SQL agent (GPT-4) connected to DuckDB
- 📈 Dynamic charts with Matplotlib/Plotly
- 📊 Analyze crypto prices, market caps, and NFT volumes
- 💬 Ask questions like:
  - *“What are the top 5 gainers this month?”*
  - *“Plot NFT volume by collection over the last 7 days”*

---

## 🛠️ Tech Stack

- **Python**
- **LangChain + OpenAI GPT-4**
- **Streamlit** for the frontend
- **DuckDB** as embedded SQL engine
- **CoinGecko API** for market data
- *(Optionally OpenSea API for NFTs)*

---

## 📂 Project Structure

```
crypto-market-explorer/
├── app/
│   └── crypto_app.py         # Streamlit frontend
├── agents/
│   └── sql_agent.py          # LangChain SQL Agent
├── scripts/
│   ├── fetch_crypto_data.py  # CoinGecko API fetcher
│   └── load_to_db.py         # Loads data into DuckDB
├── utils/
│   └── chart_gen.py          # Chart rendering utils
├── data/                     # Raw CSV storage (ignored)
├── db/                       # DuckDB storage (ignored)
├── .env                      # Your OpenAI API key (ignored)
├── requirements.txt
└── README.md
```

---

## 🔐 .env File

Create a `.env` file in your project root:

```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

✅ Don't forget to keep this private. It's already in `.gitignore`.

---

## ⚙️ Setup Instructions

```bash
# Clone the repo
git clone https://github.com/YOUR-USERNAME/crypto-market-explorer.git
cd crypto-market-explorer

# Create virtual environment
python -m venv venv
.env\Scriptsctivate

# Install dependencies
pip install -r requirements.txt
```

---

## ▶️ Run the App

```bash
# Step 1: Fetch latest data
python scripts/fetch_crypto_data.py
python scripts/load_to_db.py

# Step 2: Run Streamlit app
streamlit run app/crypto_app.py
```

---

## 🧠 Future Ideas

- Add wallet activity visualizations
- Integrate OpenSea for real NFT market tracking
- Add voice input via Whisper or HuggingFace
- Export SQL queries to CSV

---

## 🙌 Credits

- [LangChain](https://github.com/langchain-ai/langchain)
- [Streamlit](https://streamlit.io)
- [CoinGecko API](https://www.coingecko.com/en/api)

---

## 🪪 License

MIT License — feel free to fork, use, and build on top!
