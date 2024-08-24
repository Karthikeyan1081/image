import streamlit as st
import google.generativeai as genai

st.title("welcome to my app")

genai.configure(api_key="AIzaSyCBgNiey-Si0rTH5wJCH6gY03PupTwnrbI")
text =st.text_input("Enter your question")

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

if st.button("click here"):
    response = chat.send_message(text)
    st.write(response.text)