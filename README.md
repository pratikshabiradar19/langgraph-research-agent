# 🔍 LangGraph Research Agent

An agentic AI application built with LangGraph that autonomously searches the web and delivers researched answers to any question.

**Live Demo:** https://pratiksha-research-agent.streamlit.app

---

## 🧠 How It Works

This project uses a **LangGraph state graph** with two nodes connected by a conditional edge:

- **Agent Node** — Groq LLaMA 3.3 70B decides whether to search the web or answer directly
- **Tool Node** — Tavily Search fetches real-time web results
- **Conditional Edge** — routes between nodes based on whether a tool call is needed
- **State** — shared TypedDict (messages list) that persists across the full agent loop

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Agent Framework | LangGraph |
| LLM | Groq LLaMA 3.3 70B |
| Search Tool | Tavily Search API |
| LLM Orchestration | LangChain |
| Frontend | Streamlit |
| Deployment | Streamlit Cloud |

---

## 🚀 Run Locally

```bash
git clone https://github.com/pratikshabiradar19/langgraph-research-agent.git
cd langgraph-research-agent
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Create a `.env` file:
```
GROQ_API_KEY=your_groq_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

```bash
streamlit run app.py
```

---

## 👩‍💻 Author

**Pratiksha Biradar**
[LinkedIn](https://linkedin.com/in/pratiksha-biradar-979b98315) | [GitHub](https://github.com/pratikshabiradar19)

