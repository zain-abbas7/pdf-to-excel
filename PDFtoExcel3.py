import streamlit as st
import tabula
import pandas as pd
import os

def extract_tables_from_pdf(pdf_path):
    return tabula.read_pdf(pdf_path, pages="all", multiple_tables=True)

def convert_tables_to_excel(tables, excel_path):
    with pd.ExcelWriter(excel_path) as writer:
        for idx, table in enumerate(tables):
            table.to_excel(writer, sheet_name=f"Sheet{idx+1}", index=False)

# Streamlit UI
st.title("PDF to Excel Converter with Tables")

# Upload PDF file
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file:
    st.write(f"File name: {uploaded_file.name}")
    
    # Extract tables from PDF
    tables = extract_tables_from_pdf(uploaded_file)
    
    if tables:
        st.write(f"Extracted {len(tables)} table(s) from the PDF.")
        
        # Define Excel file path with the same name as the PDF
        excel_path = os.path.join(os.getcwd(), uploaded_file.name.replace('.pdf', '.xlsx'))
        
        # Convert tables to Excel
        if st.button("Convert Tables to Excel"):
            convert_tables_to_excel(tables, excel_path)
            st.success(f"Tables converted successfully! Download [here](./{excel_path.split('/')[-1]}).")
    else:
        st.warning("No tables found in the PDF.")
