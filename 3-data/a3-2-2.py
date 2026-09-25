import streamlit as st
import pandas as pd
import numpy as np
import requests

url = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/json-samples/employees.json"

response = requests.get(url) # This line sends an HTTP GET request to the specified URL and retrieves the JSON data from that URL. The response is stored in the variable 'response'.
data = response.json()

#request_path = 'employees'
# meta = [['department']]
st.write(data)

df = pd.json_normalize(data, record_path="employees", meta=["dept"])
st.dataframe(df)