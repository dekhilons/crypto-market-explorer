import os
import sys
from dotenv import load_dotenv
load_dotenv()

# Add the project root to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from agents.sql_agent import get_agent



import streamlit as st
import pandas as pd
from agents.sql_agent import get_agent
from utils.chart_gen import chart_price_change

st.title("🧠 Crypto & NFT Market Explorer")

agent = get_agent()
query = st.text_input("Ask me anything about the crypto market:")

if query:
    with st.spinner("Thinking..."):
        result = agent.run(query)
        st.markdown("### 🤖 Answer")
        st.write(result)

    if "30 days" in query and "gain" in query:
        df = pd.read_csv("data/crypto_snapshot.csv")
        path = chart_price_change(df)
        st.image(path)
