import streamlit as st
import requests

st.title("Random Poem Generator 📝")

if st.button("Generate Poem"):
    try:
        response = requests.get("https://poetrydb.org/random")
        if response.status_code == 200:
            data = response.json()
            title = data[0]["title"]
            lines = data[0]["lines"][1]
            author = data[0]["author"]
            st.success(title)
            st.success(lines)
            st.success(author)
            
    except:
        print("Error found can't load data!")


st.write("------------")
st.markdown("""
    <p style='text-align: center; color: blue; font-size: 18px;'>
        Made with 🧡 by Vikram
    </p>
""", unsafe_allow_html=True)
