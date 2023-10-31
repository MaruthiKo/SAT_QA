import streamlit as st
from langchain_helper import get_qa_chain, create_vector_db

st.title("SAT QA 🧑‍🎓")
st.caption('This QA app can currently help you with questions related to __:green[world_history]__ and  __:green[us_history]__')
# btn = st.button("Create Knowledge Base")

# if btn:
#     pass
flag = 1
question = st.text_input("Question: ")

if question:
    chain = get_qa_chain()
    response = chain(question) # returns a list of answers
    flag = 0
    st.header("Answer:")
    st.code(response["result"], language=None)

if flag:
    st.subheader("Example Question: ")
    code = '''Who developed and taught the doctrine of predestination?'''
    st.code(code, language=None)