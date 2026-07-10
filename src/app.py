import streamlit as st
import requests

st.title("RAG Chatbot")

question = st.text_input("Ask a question")

if st.button("Submit"):
    response = requests.post(
        "http://127.0.0.1:8000/ask",
        json={"question": question}
    )

    data = response.json()

    st.write("### Answer")
    st.write(data["answer"])

    st.write("### Sources")
    for source in data["sources"]:
        st.write(f"{source['file']} - Page {source['page']}")