import streamlit as st
import pandas as pd
import numpy as np


chart_data = pd.DataFrame(np.random.randn(20, 4), columns=["col1", "Angry", "Sad", "Happy"])

st.balloons()
st.header("Hi, I am Daithy")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Education")
    st.write("University of Washington - Technology Innovation")
    st.subheader("Work Experience")
    st.write("SDE internship @ DragonTesting")
    st.subheader("Hobbies")
    st.write("Sleep")
    st.subheader("Interesting project")
    st.write("none")

with col2:
    st.image('chelsey.JPG', caption='Me')
    st.link_button("LinkedIn", "https://www.linkedin.com/in/chinshanlee/", help=None, type="secondary", disabled=False, use_container_width=False)

st.divider()

st.header("My Favorite Song")
st.video("https://youtu.be/wA3mVqo-jvg?si=6fWBvft5O7-k2TcY", format="video/mp4", start_time=0)

st.divider()

st.header("My Mental Health Status")
st.line_chart(
   chart_data, x="col1", y=["Angry", "Sad", "Happy"], color=["#E07A5F", "#A9BCD0", "#F2CC8F"]
)
