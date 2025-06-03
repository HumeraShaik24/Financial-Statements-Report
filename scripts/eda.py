import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def run_eda(df):
    st.header("🔍 Exploratory Data Analysis")

    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Summary Statistics")
    st.write(df.describe(include='all'))

    st.subheader("Missing Values")
    missing = df.isnull().sum()
    st.write(missing[missing > 0])

    st.subheader("Histograms")
    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
    for col in numeric_cols:
        fig, ax = plt.subplots()
        sns.histplot(df[col].dropna(), kde=True, ax=ax)
        ax.set_title(f'Histogram of {col}')
        st.pyplot(fig)