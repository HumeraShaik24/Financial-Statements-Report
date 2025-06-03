import streamlit as st
import openai

openai.api_key = st.secrets["OPENAI_API_KEY"]

def ai_query_engine(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=150,
        temperature=0.7
    )
    return response['choices'][0]['message']['content']

def run_chat(df):
    st.header("💬 Ask the Data Copilot (GPT-powered)")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_input = st.text_input("Ask something about your data")

    if user_input:
        response = ai_query_engine(f"Analyze this DataFrame:\nColumns: {df.columns.tolist()}\nUser question: {user_input}")
        st.session_state.chat_history.append((user_input, response))

    for q, r in st.session_state.chat_history:
        st.write(f"**You:** {q}")
        st.write(f"**Copilot:** {r}")