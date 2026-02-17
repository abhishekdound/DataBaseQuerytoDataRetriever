import streamlit as st
from langchain_helper import get_few_shot_db_chain
# from google import genai
# import os

st.title("AtliQ T Shirts: Database Q&A 👕")

question = st.text_input("Question: ")

if question:
    chain = get_few_shot_db_chain()
    response = chain.invoke({"query": question})

    st.header("Answer")
    st.write(response["result"])

# def check():
#     client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])
#
#     for m in client.models.list():
#         print(m.name)
#
# if __name__ == "__main__":
#     check()






