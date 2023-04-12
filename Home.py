import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

# with col1:
    # st.image("images/photo.png")

# with col2:
st.title("Aashi Gupta")
content = """
Hi, I am Aashi Gupta! I belong to Agra, Uttar Pradesh, India. I am a passionate python programmer. Currently, I am 
pursuing B.tech in Information Technology from Galgotias College of Engineering and Technology, Greater Noida, 
Uttar Pradesh. I am passionate learner, I love to learn new things whether its related to study or any kind of art.
This website showcase my python projects which I made during learning Python. Check them out! : )
"""
st.info(content)

content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv")

with col3:
    for index, row in df[:3].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[3:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")