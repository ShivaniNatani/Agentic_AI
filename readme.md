# 🧠 Agentic AI Financial Assistant

This is a multi-agent, tool-augmented AI assistant built using the [Phi framework](https://github.com/phi-search/phi) and Groq's LLaMA3-70B model. It fetches real-time financial insights and news for any stock symbol.

## 🚀 Features
- Multi-agent architecture with role-based task routing
- Financial data using `YFinanceTools`
- News scraping using `DuckDuckGo`
- CLI and Streamlit UI
- Powered by Groq's blazing-fast LLMs

## 📦 Tech Stack
- Groq (`llama3-70b-8192`)
- Phi Framework
- YFinanceTools & DuckDuckGo
- Python, Streamlit

## 🔧 Setup
```bash
git clone https://github.com/yourusername/agentic-ai-financial-assistant.git
cd agentic-ai-financial-assistant
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
touch .env  # Add your GROQ_API_KEY here
