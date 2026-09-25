import streamlit as st
import pandas as pd

base_url = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/minimart/"

months = ['jan','feb','mar','apr']
select_month = st.radio("Select a month", months, horizontal=True)

# process
url = base_url + f"purchases-{select_month}.csv"
df = pd.read_csv(url)
df['month'] = select_month
customer_url = base_url + f"customer.csv"
customer_df = pd.read_csv(customer_url)
combined = pd.merge(df, customer_df,
                    left_on='customer_id',right_on='customer-id',
                    how='right')

# output
st.dataframe(combined)

# know when it is left, right, or full