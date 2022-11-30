import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

FILES = {
    'survey': "survey.csv",
}


st.title('Website Satisfaction Survey...')
st.write("Hatairat Teeravorawan 6416030473")
st.header('ABOUT DATASET')
st.markdown('**Conducted after using an e-commerce website. Assessed web design features (typography, color, content quality, interactivity, and navigation) and satisfaction, trust, and loyalty.**')
with st.expander("Typography", expanded=True):

    st.write(
        """   
        - q1 : It is easy to read the text on this website with the used font type and size.
        - q2 : The font color is appealing on this website.
        - q3 : The text alignment and spacing on this website make the text easy to read.
	    """
    )
with st.expander("Color", expanded=True):

    st.write(
        """  
        - q4 : The color scheme of this website is appealing.
        - q5 : The use of color or graphics enhances navigation.
	    """
    )
with st.expander("Content/information quality", expanded=True):

    st.write(
        """  
        - q6 : The information content helps in buying decisions by comparing the information about products or services.
        - q7 : The information content provided by this website meets my needs.
        - q8 : Contents and information support for reading and learning about buying process.
	    """
    )
with st.expander("Interactivity", expanded=True):

    st.write(
        """  
        - q9 : This website provides adequate feedback to assess my progression when I perform a task.
        - q10 : This website offers customization.
        - q11 : This website offers versatility of ordering process.
        - q12 : This website provides content tailored to the individual.
        - q13 : In this website everything is consistent.
   	    """
    )
with st.expander("Navigation", expanded=True):

    st.write(
        """  
        - q14 : Navigation aids serve as a logical road map for buying.
        - q15 : Obviousness of buying button and links in this website.
        - q16 : It is easy to personalize or to narrow buying process.
        - q17 : It is easy to learn to use the website.
        - q18 : This website supports reversibility of action.
   	    """
    )
with st.expander("Satisfaction", expanded=True):

    st.write(
        """  
        - q19 : Overall I am satisfied with the interface of this website.
        - q20 : My current experience with this website is satisfactory.
        - q21 : Overall. I am satisfied with the amount of time it took to complete the tasks for buying products.
        - q22 : Overall. I am satisfied with accuracy for this website related to the buying process.
   	    """
    )
with st.expander("Trust", expanded=True):

    st.write(
        """  
        - q23 : I trust the information presented on this website.
        - q24 : This website is credible for me.     
   	    """
    )
with st.expander("Loyalty", expanded=True):

    st.write(
        """  
        - q25 : I would visit this website again.
        - q26 : I would recommend this website to my friend.
   	    """
    )


with st.sidebar:
    selectfile = st.radio(
        "Choose a CSV file",
        FILES.keys()
    )
    st.write(selectfile)



selectedfile = FILES[selectfile]
df = pd.read_csv('survey.csv')
df.columns = ["User","Lanquage","Platform",
                "Gender", "Age","q1","q2",
                "q3", "q4", "q5", "q6", "q7", "q8",
                "q9", "q10", "q11", "q12", "q13", "q14",
                "q15", "q16", "q17", "q18", "q19", "q20",
                "q21", "q22", "q23", "q24", "q25", "q26"]

@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

csv = convert_df(df)

st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='survey.csv',
    mime='text/csv',
)

st.dataframe(df)


if selectfile == "survey":
    
    st.header("แสดงข้อมูลจำนวนตามการแบ่งกลุ่ม")
    option = st.selectbox('เลือก Column', df.columns)
    st.write('คุณเลือก:', option)
    fig, ax = plt.subplots(figsize=(10,5))
    sns.countplot(x=df[option])
    st.pyplot(fig)


    st.header("แสดงความสัมพันธ์")
    option_x = st.radio(
    'เลือกแกน X',
    ["Age", "Gender"])
    option_y = st.radio(
    'เลือกแกน Y',
    ["Age", "Gender"])
    option_hue = st.radio(
    'เลือก hue',
    ["q1", "q2"])

    fig, ax = plt.subplots(figsize=(20,10))
    sns.scatterplot(x=option_x, y=option_y,
                    linewidth=0,
                    data=df, hue=option_hue,
                    style="Overall Height")
    st.pyplot(fig)



else:
    pass
                


