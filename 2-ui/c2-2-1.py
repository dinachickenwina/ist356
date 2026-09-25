import streamlit as st

# Title
st.title("Area and Perimeter Calculator")

# Input
length = st.number_input("Enter the length of the rectangle:", min_value=0.0, step=0.1)
width = st.number_input("Enter the width of the rectangle:", min_value=0.0, step=0.1)

# Calculate area and perimeter
area = length * width
perimeter = 2 * (length + width)

# Output
st.write(f"The area of the rectangle is: {area}")
st.write(f"The perimeter of the rectangle is: {perimeter}")

# Debug and run the app using the following command in your terminal: python -m streamlit run 2-ui/c2-2-1.py