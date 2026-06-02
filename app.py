# app.py

import streamlit as st
from agent import run_agent

st.set_page_config(page_title="Research Agent", page_icon="🔍")
st.title("🔍 Research Agent")
st.caption("Powered by LangGraph + Groq (Llama 3.3) + Tavily Search")

if "history" not in st.session_state:
    st.session_state.history = []

for msg in st.session_state.history:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if question := st.chat_input("Ask me anything — I'll search the web for you"):

    st.session_state.history.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.write(question)

    with st.chat_message("assistant"):
        with st.spinner("Thinking and searching..."):
            answer = run_agent(question)
        st.write(answer)

    st.session_state.history.append({"role": "assistant", "content": answer})