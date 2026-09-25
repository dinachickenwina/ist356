import streamlit as st
import pandas as pd 
import numpy as np

# This file is semicolon-delimited and does not include column names.
url = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/delimited/students-no-header-blanks.ssv"

# Skip the five descriptive lines, then provide names for the headerless data.
data = pd.read_csv(
	url,
	skiprows=5,
	header=None,
	sep=";",
	names=["Name", "Grade", "Year"],
)

# This line displays the DataFrame 'data' in the Streamlit app. The st.dataframe() function is used to render the DataFrame as an interactive table in the web application, allowing users to view and explore the data.
st.dataframe(data) 
