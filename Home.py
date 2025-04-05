import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("The Best Company")

content = '''
World-Class Universities – The U.S. is home to many globally ranked universities like Harvard, MIT, and Stanford, offering top-tier education and research opportunities.
Better Infrastructure – American universities have advanced labs, libraries, and classrooms, providing students with state-of-the-art resources.
Flexible Curriculum – Unlike India’s rigid education system, U.S. institutions allow students to explore multiple subjects before choosing a major.
'''
st.write(content)

st.header("Our Team")

df = pd.read_csv("data.csv")
col1, col2, col3 = st.columns(3)

with col1:
    for index, row in df[0:4].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"].title())
        st.image("images/"+row["image"])

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"].title())
        st.image("images/"+row["image"])

with col3:
    for index, row in df[8:].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"].title())
        st.image("images/"+row["image"])