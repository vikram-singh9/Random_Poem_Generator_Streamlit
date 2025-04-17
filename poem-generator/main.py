import streamlit as st
import requests
st.title("Random Poem Generator 📝")

if st.button("Generate Poem"):
    try:
        response = requests.get("https://poetrydb.org/random")
        if response.status_code == 200:
            data = response.json()
            print (data)
    except:
        print("Error found can't load data!")