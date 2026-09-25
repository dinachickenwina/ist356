import streamlit as st

st.title("Streamlit Interaction: linear")

# setup
name = st.text_input("Who are you?")
hi_clicked = st.button('Say Hi!')
clear_clicked = st.button('Clear')

# interactions
if hi_clicked:
    if name:
        st.success(f"Hello, {name}", icon="👍")
        # Emoji keyboard = Windows button + . (period) or Mac Control + Command + Space
    else:
        st.error(f"I can't say hello, if you don't tell me your name!", icon="💣")
else:
    # Someone didn't click the hi, but streamlit ran
    # Downside of streamlit is that it runs the whole script every time you interact with the app, so you have to be careful with your code.

if clear_clicked:
    name = None 
