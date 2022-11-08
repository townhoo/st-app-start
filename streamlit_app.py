import streamlit as st
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

st.title('AR686')
st.write("Web App นี้เป็นส่วนหนึ่งของวิชา AR686 คณะสถาปัตยกรรมศาสตร์มหาวิทยาลัยธรรมศาสตร์")
df = pd.read_csv('StudentsPerformance.csv')

st.write(df)

option = st.selectbox("เลือก Col ที่ต้องการแสดง Group", df.columns)

fig = plt.figure(figsize=(10, 4))
sns.countplot(x=df[option])

st.write("""
# แสดงกราฟ

อธิบาย xxx
""")
st.pyplot(fig)



st.write("""
# Scatter Plot

อธิบาย xxx
""")
fig = plt.figure(figsize=(10, 4))
sns.scatterplot(x="math score", y="reading score", data=df)

st.pyplot(fig)

#st.write()