import streamlit as st
from fpdf import FPDF
import os

def create_pdf(df):
    st.header("📝 Generate PDF Report")
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, "Data Analyst Copilot Report", ln=True, align='C')

    pdf.set_font("Arial", '', 12)
    pdf.ln(10)
    pdf.cell(200, 10, f"Shape of dataset: {df.shape}", ln=True)

    pdf.ln(5)
    pdf.cell(200, 10, "Column Summary:", ln=True)
    for col in df.columns:
        dtype = str(df[col].dtype)
        nulls = df[col].isnull().sum()
        pdf.cell(200, 10, f"- {col}: {dtype}, Missing: {nulls}", ln=True)

    # Save to file
    save_path = "reports/eda_report.pdf"
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    pdf.output(save_path)

    with open(save_path, "rb") as f:
        st.download_button("📥 Download Report", f, file_name="EDA_Report.pdf", mime="application/pdf")