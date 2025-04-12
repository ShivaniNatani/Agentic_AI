from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
import os

# ✅ Load environment variables
load_dotenv()

# ✅ Get Groq API Key
groq_key = os.getenv("GROQ_API_KEY")
print("🔐 Loaded GROQ_API_KEY:", groq_key[:12] + "..." if groq_key else "❌ Not found")
assert groq_key and groq_key.startswith("gsk_"), "❌ GROQ_API_KEY missing or invalid in .env"

# ✅ Web Search Agent
web_search_agent = Agent(
    name="web_search_agent",
    role="Search the web for information",
    model=Groq(id="llama3-70b-8192", api_key=groq_key),
    tools=[DuckDuckGo()],
    instructions=["Always include sources when providing information."],
    show_tool_calls=True,
    markdown=True,
)

# ✅ Financial Agent
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

# ✅ Combined Multi-Agent
multi_ai_agent = Agent(
    team=[web_search_agent, finance_agent],
    model=Groq(id="llama3-70b-8192", api_key=groq_key),
    instructions=["Always include sources", "Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

# ✅ Ask a financial+news question
multi_ai_agent.print_response(
    "Get the latest analyst recommendations using financial data tools, and fetch recent news articles using web search tools for NVDA. Include clear sections with titles and format financial insights as tables.",
    stream=True
)

#SAVE THE RESPONSE
response = multi_ai_agent.run("...")
with open("nvda_summary.md", "w") as f:
    f.write(response.content)


