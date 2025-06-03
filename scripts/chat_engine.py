import streamlit as st
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Function to get AI-generated response
def ai_query_engine(prompt):
    response = client.chat.completions.create(
        model="gpt-4o",  # or "gpt-4", "gpt-3.5-turbo"
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant for data analysis."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content

# Streamlit chat interaction
def run_chat(df):
    st.subheader("🧠 AI Chat Assistant")
    st.markdown("Ask questions about your dataset!")

    if df is not None:
        user_input = st.text_input("Ask a question about the dataset:")

        if user_input:
            with st.spinner("Analyzing..."):
                # Build the prompt with DataFrame column info
                prompt = f"Analyze this DataFrame:\nColumns: {df.columns.tolist()}\nUser question: {user_input}"
                response = ai_query_engine(prompt)
                st.success("Response:")
                st.write(response)
