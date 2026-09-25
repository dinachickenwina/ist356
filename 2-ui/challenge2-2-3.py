# Challenge 2-2-3: Order File processing
# Write a streamlit to input a text file with one line per order. 
# Samples are provided in the `data` folder, but each line should have the amount of the order.
# Output the number of orders and the total amount of all orders.

import streamlit as st

st.title("Order Processor")

# Initialize variables
total = 0.0
count = 0

# Input
file = st.file_uploader("Upload Text File:", 
                        type=["txt"]) # Input for the text file

# Process
if file is not None:
    for line in file:
        amount = float(line.strip())
        total += amount
        count += 1
    except ValueError:
        st.error("Invalid amount in file. Please ensure each line contains a valid number.")
    
# Output
st.write(f"Total Amount: {total}")
st.write(f"Total Orders: {count}")