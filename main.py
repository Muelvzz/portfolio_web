import streamlit as st
import pandas

st.set_page_config(layout='wide')

st.title("My Personal Portfolio")

col1, col2 = st.columns(2)

with col1:
    st.image("images/2x2.jpg", width=350)

with col2:
    st.title("Muelvin Lopez")
    content = "I am an incoming freshman pursuing Computer Science. This is my very first publication of my personal website, am incredible milestone for an aspiring programmer such as I who is aiming to break into this field. In my high school years, I graduated with flying colors - I became the only with highest honor student of my capus since I was on my 11th grade, and on 12th grade as well.  This website would not be possible without the mentorship of Sir. Ardit."
    st.info(content)

content2 = "If there are any questions, and concerns - feel free to let me know in my email or in my social media accounts."
st.info(content2)

col3, empty_col, col4 = st.columns([2, 0.3, 2])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")


with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
