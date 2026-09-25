# Write a streamlit to input an amount.
# Create an "add to total" button to accumulate the amount in the total. 
# Create a "clear" button to reset the session vars. 
# Display the total and the history of each item entered. 
# HINT: you'll need to manage a list for history!

# A session state is a way to store variables across reruns of the app. 
# If you want to remember a variable, you can store it in the session state.
# Every time an event triggers, the app reruns, and all variables are reset to their initial values.

import streamlit as st

st.title("Order Tracker")

# Initialize variables
if 'total' not in st.session_state:
    st.session_state.total = 0
    st.session_state.history = []

# Inputs
amount = st.number_input("Order Amount:") # Input for the order amount
total_button = st.button("Calculate Total", 
                         type="primary") # Button to calculate the total
clear_button = st.button("Clear") # Button to clear the total and history

# Process - Avoid outputting, just manipulate data
if total_button:
    st.session_state.total += amount # += means add to the total
    st.session_state.history.append(amount) # Append is a list operation, means add to the list

if clear_button:
    st.session_state.total = 0 # Reset the total to 0
    st.session_state.history = [] # Reset the history to an empty list
    st.session_state.amount = 0 # Reset the amount to 0

# Outputs
st.write(f"Total Order: {st.session_state.total}")
st.write(f"History: {st.session_state.history}")