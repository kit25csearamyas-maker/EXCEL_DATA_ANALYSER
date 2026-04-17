
import streamlit as st
import pandas as pd

st.title("📊 Excel Data Analyzer")

uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    
    st.subheader("📋 Data Preview")
    st.dataframe(df)

    total = df["Marks"].sum()
    average = df["Marks"].mean()
    highest = df["Marks"].max()
    lowest = df["Marks"].min()

    def grade(mark):
        if mark >= 90:
            return "A"
        elif mark >= 75:
            return "B"
        elif mark >= 50:
            return "C"
        else:
            return "Fail"

    df["Grade"] = df["Marks"].apply(grade)

    st.subheader("📊 Analysis")
    st.write("Total Marks:", total)
    st.write("Average Marks:", average)
    st.write("Highest Mark:", highest)
    st.write("Lowest Mark:", lowest)

    st.subheader("🏆 Updated Data with Grades")
    st.dataframe(df)
    
    #cd ExcelProject/DataAnalyzer
    #streamlit run app.py
