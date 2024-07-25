import streamlit as st

st.set_page_config(layout="wide")

col1,  col2 = st.columns(2)

with col1:
    st.image("images/img1.png", width=400)

with col2:
    st.title("Nitish Kumar Saw")
    st.write("""Hello! My name is Nitish, and I am currently pursuing a degree in Information Technology.
             I have a passion for technology and problem-solving, and I am particularly interested in areas such as software
             development, network security, and data analysis. Throughout my studies, I have gained hands-on experience with 
             programming languages like Java and Python, and I am eager to continue expanding my skills and knowledge. I look forward
             to contributing to innovative projects and collaborating with others in the tech industry.""")

st.header("Kuku this is my message for you.")

cont = """I know you are trying hard to make me happy. Keep going on I am always here to support you.
             You are a great human being. There are some plus and negative points for every individual even I have my own
             plus and negative points. But we both are here to accept each other. Don't take a lot of stress and try to
             be calm.
             Let's build our home together!!"""
st.write(cont)
cont2 = """ This world is not our concern. We are not here to make others happy or sad. Just focus on yourself and you can focus on me.........."""

st.header(cont2)


col3, col4 = st.columns(2)
with col3:
    st.image("images/img2.png", width=500)
with col4:
    st.image("images/img3.png", width=500)







