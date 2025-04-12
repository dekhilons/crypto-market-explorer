import duckdb
import pandas as pd

df = pd.read_csv("data/crypto_snapshot.csv")
con = duckdb.connect(database='db/crypto.db', read_only=False)
con.execute("DROP TABLE IF EXISTS crypto_data;")
con.execute("""
CREATE TABLE crypto_data AS 
SELECT * FROM df
""")
con.close()
