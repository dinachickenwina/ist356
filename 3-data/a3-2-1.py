import streamlit as st
import pandas as pd 
import numpy as np

url = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/delimited/webtraffic.log"

data = pd.read_csv(url, sep=" ", skiprows=3)

st.dataframe(data) 

# If you look at the header it gives away what the separator is, so you can use that to determine the correct separator for reading the file. In this case, the header indicates that the separator is a pipe (|), so you would need to specify sep='|' when reading the file with pd.read_csv().