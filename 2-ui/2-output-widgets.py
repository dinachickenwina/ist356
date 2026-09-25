import streamlit as st

st.title('Streamlit Output Widgets!')

st.markdown("## Text Output")
st.text("Plain text.\nObeys newlines.")

st.markdown("## Markdown Output")
st.markdown('''
### Heading 3
- this
- is a
- list
            
Learn markdown here: [https://www.markdownguide.org/getting-started/](https://www.markdownguide.org/getting-started/)
''')

st.markdown("## Code Output")
st.code('''
name = input("Enter your name:")
print(f"Hello, {name}")
''', language="python", line_numbers=True)

# Image output is a way to display images in your app. This is useful for providing visual context or information to the user, or for creating a more engaging experience.
st.markdown("## Image Output")
st.image("https://ist256.com/images/logo.png",caption="IST256 logo") # Display the IST256 logo given the URL. You can also use a local file path, e.g. st.image("images/logo.png", caption="IST256 logo")

# Metric / Card Output is a way to display key performance indicators (KPIs) or other important metrics in a visually appealing way. This is useful for providing quick insights into the performance of your app or business.
st.markdown("## Metric / Card Ouput")
st.metric(label="Temperature", 
          value="70 °F", 
          delta="1.2 °F")
st.metric(label="Mike Fudge", value="B+", delta="-5 pts")

# Video and audio output are ways to display multimedia content in your app. This is useful for providing additional context or information to the user, or for creating a more engaging experience.
st.markdown("## Video Output")
st.video("https://youtu.be/soVItkifdms?si=eNNbRXnAg4efcJGi")

st.markdown("## Audio Output")
st.audio("https://file-examples.com/storage/fe6993554766e3161a375a5/2017/11/file_example_MP3_700KB.mp3")

# Toast output is a way to display a temporary message to the user. This is useful for providing feedback on an action that the user has taken, such as clicking a button or submitting a form.
st.markdown("## Toast Output")
if st.button("Click to show toast"):
    st.toast("Congrats! You clicked it!", icon=":material/thumb_up:")

# Columns are a way to organize content into separate vertical sections. This is useful for creating a more visually appealing layout and for grouping related content together.
st.markdown("## Column Layouts")
col1, col2, col3 = st.columns(3)
col1.markdown("Hello")
col2.text("There")
col2.text("Mike")
col3.warning("Warning!")
col3.error("Error!")
col3.success("Success!")

# Tabs are a way to organize content into separate views that can be switched between. This is useful for grouping related content together and allowing the user to focus on one view at a time.
st.markdown("## Tab Layouts")
col1, col2, col3 = st.tabs(["Tab A","Tab B","Tab C"])
col1.markdown("Hello")
col2.text("There")
col2.text("Mike")
col3.warning("Warning!")
col3.error("Error!")
col3.success("Success!")

# Expander output is a way to hide content until the user clicks to expand it. This is useful for long content that you don't want to overwhelm the user with at first glance.
st.markdown("## Expander Output")
with st.expander("See a map"):
    st.write('Here is a map for you!')
    st.map(latitude=76,longitude=-43, zoom=13)