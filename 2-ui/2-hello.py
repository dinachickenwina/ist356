# To make changes to the app, you can edit the code and save it (CTRL + S). The app will automatically reload and reflect the changes in the browser.

import streamlit as st # Alias as st

st.title("Saying Hello.")
name = st.text_input("And you are?")
age = st.slider("How old are you?", min_value=18, max_value=35, value=(35+18//2), step=1)  # Slider to select age

mybutton = st.button("Activate") # Button to activate the input

if mybutton: # If button is pressed
    st.write(f"Hello, {name}!") # Writing to streamlit
    st.write(f"You are {age} years old!") # Writing to streamlit

# Won't work because when you run streamlit you have to run a web server, so you can see the output in your browser.
# Type the following command in your terminal to run the app: python -m streamlit run 2-ui/2-hello.py
# Enter email -> Pop-up in browser -> http://localhost:8501/ -> Manually add the 1 -> http://localhost:18501/
# Run and debug -> Streamlit Run Dropdown -> Run

