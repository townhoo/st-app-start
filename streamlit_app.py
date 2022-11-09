import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

FILES = {
    'Student Performance': "StudentsPerformance.csv",
    "Building Data": "buildingdata.csv",
    "ENB2012": "ENB2012_data.xlsx"
}

st.write("Web App นี้เป็นส่วนหนึ่งของวิชา AR686 คณะสถาปัตยกรรมศาสตร์มหาวิทยาลัยธรรมศาสตร์")
with st.sidebar:
    selectfile = st.radio(
        "Choose a CSV file",
        FILES.keys()
    )
    st.write(selectfile)

selectedfile = FILES[selectfile]

st.title(selectfile)
if selectfile == "ENB2012":
    df = pd.read_excel(selectedfile)
else:
    df = pd.read_csv(selectedfile)
st.dataframe(df)

if selectfile == "Student Performance":
    st.title("แสดงค่าเฉลี่ยของคะแนนทั้ง 3 วิชา")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("เลข")
        fig, ax = plt.subplots()
        ax.hist(df['math score'], bins=20)
        st.pyplot(fig)
    with col2:
        st.subheader("อ่าน")
        fig, ax = plt.subplots()
        ax.hist(df['reading score'], bins=20)
        st.pyplot(fig)
    with col3:
        st.subheader("เขียน")
        fig, ax = plt.subplots()
        ax.hist(df['writing score'], bins=20)
        st.pyplot(fig)
    
    st.header("แสดงข้อมูลจำนวนตามการแบ่งกลุ่ม")
    option = st.selectbox('เลือกชื่อ Column', df.columns)
    st.write('คุณเลือก:', option)
    fig, ax = plt.subplots(figsize=(10,5))
    sns.countplot(x=df[option])
    st.pyplot(fig)

    st.header("แสดงความสัมพันธ์ของคะแนน")
    option_x = st.radio(
    'เลือกแกน X',
    ["math score", "reading score", "writing score"])
    option_y = st.radio(
    'เลือกแกน Y',
    ["math score", "reading score", "writing score"])

    fig, ax = plt.subplots(figsize=(10,5))
    sns.scatterplot(x=option_x, y=option_y,
                    linewidth=0,
                    data=df, hue="gender")
    st.pyplot(fig)

    fig = sns.displot(data=df, x="reading score", hue="gender")
    st.pyplot(fig)
else:
    pass