# Streamlit is a framework for building web apps in Python. 
# It is used to create interactive data visualizations and dashboards.
import streamlit as st 

# Pandas is a library for data manipulation and analysis. 
# It provides data structures and functions needed to manipulate structured data seamlessly. 
import pandas as pd

# Numpy is a library for numerical computing in Python. 
# It provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays.
import numpy as np





# Create a pandas Series with data and index
index = ['a','b','c','d']
s1_series = pd.Series(data=[1,2,3,4], 
                      dtype=int,index=index, name='s1') #dtype=int specifies that the data type of the Series is integer
s2_series = pd.Series(data=[2.2, np.nan, 3.0, 1.5], 
                      dtype=np.float64,index=index, name='s2') # float64 is a data type that represents a 64-bit floating point number. np.nan is used to represent missing values in the Series.
s3_series = pd.Series(data=['q','q','z','z'], 
                      index=index, name='s3')





# List of Series is converted to a DataFrame
# .T transposes the DataFrame, swapping rows and columns, so that the Series become columns in the DataFrame.
df = pd.DataFrame ({"s1": s1_series, "s2": s2_series, "s3": s3_series}).T

st.dataframe(df) # Basic stats in datafram format
st.dataframe(df.describe()) # Display the basic statistics of the DataFrame in the Streamlit app

print(df.info()) # Display the DataFrame info in the Streamlit app

