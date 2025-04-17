import streamlit as st
import requests

st.title("Random Poem Generator 📝")

if st.button("Generate Poem"):
    try:
        response = requests.get("https://poetrydb.org/random")
        if response.status_code == 200:
            data = response.json()
            title = data[0]["title"]
            lines = data[0]["lines"]
            author = data[0]["author"]

            result = title, lines, author
            st.success(result)
            # st.success(lines)
            # st.success(author)
            
            
    except:
        print("Error found can't load data!")