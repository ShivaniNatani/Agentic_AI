import streamlit as st
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()
groq_key = os.getenv("GROQ_API_KEY")

# Streamlit UI
st.set_page_config(page_title="📈 Financial AI Agent", layout="wide")
st.title("🧠 Financial AI Assistant")
st.markdown("Ask about any stock and get analyst insights + latest news from the web.")

# Input
stock_symbol = st.text_input("Enter Stock Symbol (e.g., NVDA, TSLA, AAPL)", value="NVDA")

# Set up Agents
web_search_agent = Agent(
    name="web_search_agent",
    role="Search the web for information",
    model=Groq(id="llama3-70b-8192", api_key=groq_key),
    tools=[DuckDuckGo()],
    instructions=["Always include sources when providing information."],
    show_tool_calls=True,
    markdown=True,
)

finance_agent = Agent(
    name="finance_AI_agent",
    role="Get financial data",
    model=Groq(id="llama3-70b-8192", api_key=groq_key),
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            stock_fundamentals=True,
            company_news=True,
        )
    ],
    instructions=["Use tables to display the data."],
    show_tool_calls=True,
    markdown=True,
)

# Combine agents
multi_ai_agent = Agent(
    team=[web_search_agent, finance_agent],
    model=Groq(id="llama3-70b-8192", api_key=groq_key),
    instructions=["Always include sources", "Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

# Button
if st.button("🔍 Analyze"):
    query = f"Get the latest analyst recommendations using financial data tools, and fetch recent news articles using web search tools for {stock_symbol}. Include clear sections with titles and format financial insights as tables."
    with st.spinner("Running agents..."):
        result = multi_ai_agent.run(query)
        st.markdown(result.content)
