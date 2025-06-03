import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def run_eda(df):
    st.subheader("📊 Exploratory Data Analysis")

    # Data Summary
    st.write("### Data Snapshot")
    st.dataframe(df.head())

    st.write("### Data Types")
    st.write(df.dtypes)

    st.write("### Null Values")
    st.write(df.isnull().sum())

    st.write("### Descriptive Statistics")
    st.write(df.describe())

    # Dynamic visualizations
    st.write("### Visualizations")
    numeric_cols = df.select_dtypes(include=['number']).columns
    categorical_cols = df.select_dtypes(include=['object', 'category', 'bool']).columns

    if st.checkbox("Show Histograms for Numeric Columns"):
        for col in numeric_cols:
            fig, ax = plt.subplots()
            df[col].hist(ax=ax, bins=20)
            ax.set_title(f"Histogram of {col}")
            st.pyplot(fig)

    if st.checkbox("Show Box Plots"):
        for col in numeric_cols:
            fig, ax = plt.subplots()
            sns.boxplot(data=df[col], ax=ax)
            ax.set_title(f"Boxplot of {col}")
            st.pyplot(fig)

    if st.checkbox("Show Bar Charts for Categorical Columns"):
        for col in categorical_cols:
            fig, ax = plt.subplots()
            df[col].value_counts().plot(kind='bar', ax=ax)
            ax.set_title(f"Bar chart of {col}")
            st.pyplot(fig)

    if st.checkbox("Show Correlation Heatmap"):
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.heatmap(df[numeric_cols].corr(), annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)

    if st.checkbox("Show Pairplot (sampled if large)"):
        if len(df) > 500:
            st.info("Showing pairplot on a sample of 500 rows to improve speed.")
            df_sample = df.sample(500)
        else:
            df_sample = df
        sns.pairplot(df_sample[numeric_cols])
        st.pyplot()
