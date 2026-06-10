# 🤖 LangGraph Research Agent

> Autonomous AI research agent that decides in real-time whether to search the web or answer directly — built with LangGraph state graphs, Groq LLaMA 3.3 70B, and Tavily Search API.

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit)](https://pratiksha-research-agent.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python)](https://python.org)
[![LangGraph](https://img.shields.io/badge/LangGraph-0.2-1C3C3C?style=for-the-badge)](https://langchain-ai.github.io/langgraph/)

---

## What makes this different from a basic chatbot

Most LLM apps are linear: input → LLM → output. This agent uses a **stateful graph** where the agent reasons at each step and decides which path to take — search the web or answer from its own knowledge.

```
User Query
    │
    ▼
┌─────────────────────────────────────────────┐
│           LangGraph StateGraph              │
│                                             │
│   [agent_node] ──── needs search? ────────► [search_node]
│       ▲                                          │
│       │  no search needed                        │
│       │                                          │
│   [END] ◄──────────────────────────────────────┘
│         (answer from memory or search result)    │
└─────────────────────────────────────────────┘
         │
         ▼
    TypedDict State
    (full message history
     persists across loops)
```

**Why LangGraph instead of ReAct agents?**
LangGraph gives you an explicit, debuggable state graph with deterministic routing. ReAct agents are less predictable — you can't see exactly which path was taken. LangGraph makes the decision logic visible and testable.

---

## Architecture

| Component | Technology | Why this choice |
|-----------|-----------|-----------------|
| Agent framework | LangGraph StateGraph | Stateful, cyclic graph — enables loops and conditional branching |
| LLM | Groq LLaMA 3.3 70B | Fast inference (~200 tok/s), free tier, strong reasoning |
| Web search | Tavily Search API | Built for LLM agents — returns clean, structured results |
| State management | TypedDict | Typed, persistent message history across agent loop iterations |
| Frontend | Streamlit | Rapid deployment, shareable live demo |

---

## Key technical decisions

**Conditional edge routing** — The agent node outputs either `"search"` or `"end"`. LangGraph routes to the appropriate node based on this output. This is the core of what makes it agentic rather than just a chain.

**Shared TypedDict state** — Every node reads from and writes to the same state object. The full message history is preserved across every iteration of the loop — the agent "remembers" everything it has done in the current session.

**Tool binding** — Tavily Search is bound as a tool to the LLM. The model decides when to invoke it based on the user's query. No hardcoded trigger words — pure model reasoning.

---

## Run locally

```bash
# Clone
git clone https://github.com/pratikshabiradar19/langgraph-research-agent.git
cd langgraph-research-agent

# Install
pip install -r requirements.txt

# Set environment variables
cp .env.example .env
# Add GROQ_API_KEY and TAVILY_API_KEY to .env

# Run
streamlit run app.py
```

---

## Project structure

```
langgraph-research-agent/
├── app.py              # Streamlit UI
├── agent.py            # LangGraph graph definition — nodes, edges, state
├── tools.py            # Tavily search tool binding
├── requirements.txt
└── .env.example
```

---

## Tech stack

`LangGraph` `LangChain` `Groq LLaMA 3.3 70B` `Tavily Search API` `Python` `Streamlit`

---

*Built by [Pratiksha Biradar](https://github.com/pratikshabiradar19) — Gen AI Engineer*
