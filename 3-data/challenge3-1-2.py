import streamlit as st
import pandas as pd
import numpy as np

url = "https://raw.githubusercontent.com/mafudge/datasets/master/customers/customers.csv"
# df = pd.read_csv(url)
df = pd.read_csv(url,sep=",",header=0) # header=0 specifies that the first row of the CSV file contains the column names.





# Anti-pattern: Using st.dataframe() to display the entire DataFrame can be inefficient for large datasets. Instead, consider using st.data_editor() for better performance and interactivity.
# Do not do anti-pattern: Using st.dataframe() to display the entire DataFrame can be inefficient for large datasets. Instead, consider using st.data_editor() for better performance and interactivity.

# Always use new variable after transformation, do not overwrite the original variable. 
# This helps to keep the original data intact and allows for easier debugging and reproducibility of the code.
df_ny = df[df['State'] == 'NY'] # Filter the DataFrame to include only rows where the 'state' column is 'NY'.
df_ny_info = df_ny[['First','Last','Gender','State','Total Purchased']] # Select specific columns from the filtered DataFrame for further analysis or display.






st.dataframe(df) # Display the original DataFrame in the Streamlit app
st.dataframe(df_ny) # Display the filtered DataFrame (only rows where 'state' is 'NY') in the Streamlit app
st.dataframe(df_ny_info) # Display the filtered DataFrame (only rows where 'state' is 'NY') in the Streamlit app