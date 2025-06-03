import streamlit as st
from scripts import eda, ml_utils, pdf_generator, chat_engine, voice_utils

st.set_page_config(page_title="Data Analyst Copilot", layout="wide")

st.title("🤖 Data Analyst Copilot")

uploaded_file = st.file_uploader("Upload your CSV data file", type=["csv"])

if uploaded_file:
    import pandas as pd
    df = pd.read_csv(uploaded_file)
    st.success(f"Loaded dataset with {df.shape[0]} rows and {df.shape[1]} columns.")

    # Run EDA
    eda.run_eda(df)

    # Train ML model
    ml_utils.run_ml(df)

    # PDF Report Generation
    pdf_generator.create_pdf(df)

    # Chatbot with AI
    chat_engine.run_chat(df)

    # Voice interaction example
    if st.button("🎤 Speak to Data Copilot"):
        question = voice_utils.recognize_speech()
        st.write(f"You said: {question}")
        answer = chat_engine.ai_query_engine(f"Data columns: {df.columns.tolist()}\nQuestion: {question}")
        st.write(f"Copilot says: {answer}")
        voice_utils.speak_text(answer)
else:
    st.info("Please upload a CSV file to start the analysis.")