# agent.py

import os
from dotenv import load_dotenv
from typing import TypedDict, Annotated
import operator

from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import HumanMessage, BaseMessage
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode

load_dotenv()

# ── STEP A: Define State ──────────────────────────────────────────
class AgentState(TypedDict):
    messages: Annotated[list[BaseMessage], operator.add]

# ── STEP B: Define Tools ──────────────────────────────────────────
search_tool = TavilySearchResults(max_results=3)
tools = [search_tool]

# ── STEP C: Define the LLM ───────────────────────────────────────
llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)
llm_with_tools = llm.bind_tools(tools)

# ── STEP D: Define Nodes ──────────────────────────────────────────
def agent_node(state: AgentState):
    messages = state["messages"]
    response = llm_with_tools.invoke(messages)
    return {"messages": [response]}

def should_continue(state: AgentState):
    last_message = state["messages"][-1]
    if last_message.tool_calls:
        return "tools"
    return "end"

tool_node = ToolNode(tools)

# ── STEP E: Build the Graph ───────────────────────────────────────
def build_agent():
    graph = StateGraph(AgentState)

    graph.add_node("agent", agent_node)
    graph.add_node("tools", tool_node)

    graph.set_entry_point("agent")

    graph.add_conditional_edges(
        "agent",
        should_continue,
        {
            "tools": "tools",
            "end": END
        }
    )

    graph.add_edge("tools", "agent")

    return graph.compile()

agent = build_agent()

# ── STEP F: Run the agent ─────────────────────────────────────────
def run_agent(user_question: str):
    result = agent.invoke({
        "messages": [HumanMessage(content=user_question)]
    })
    return result["messages"][-1].content