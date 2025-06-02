import streamlit as st

st.set_page_config(layout='wide')

st.title("My Personal Portfolio")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Muelvin Lopez")
    content = "I am an incoming freshman pursuing Computer Science. This is my very first publication of my personal website. This website would not be possible without the mentorship of Sir. Ardit. If there are any questions, and concerns - feel free to let me know in my email or in my social media accounts."
    st.info(content)
