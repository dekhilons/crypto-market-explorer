import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Get the API key
openai_api_key = os.getenv("OPENAI_API_KEY")

if not openai_api_key:
    raise ValueError("❌ OPENAI_API_KEY not found! Make sure your .env file is in the project root and properly formatted.")

# LangChain imports (updated to new structure)
from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_community.utilities import SQLDatabase
from langchain_community.chat_models import ChatOpenAI


def get_agent():
    # Connect to DuckDB
    db = SQLDatabase.from_uri("duckdb:///db/crypto.db")

    # Create LLM with the loaded API key
    llm = ChatOpenAI(
        temperature=0,
        model="gpt-4",
        openai_api_key=openai_api_key
    )

    # Set up the SQL toolkit
    toolkit = SQLDatabaseToolkit(db=db, llm=llm)

    # Create the SQL agent
    agent_executor = create_sql_agent(
        llm=llm,
        toolkit=toolkit,
        verbose=True
    )

    return agent_executor
