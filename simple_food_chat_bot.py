from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
st.title("🍲 Food AI Assistant\n Ask me anything about food! If you ask about something else, I'll let you know I don't know.")

system_prompt = "You are a helpful assistant and you should answer questions only on food related." \
" If asked anything else, respond I don't know."

human_input = st.text_input("Your Question")

prompt  = ChatPromptTemplate([("system", system_prompt), 
                    ("human", "{question}")])

chain = prompt | llm | StrOutputParser()

submit_button = st.button("Submit")

if submit_button and human_input:
    try:
        response = chain.invoke({"question":human_input})
        st.subheader("Response:")
        st.info(response)
    except Exception as e:
        st.error(f"An error occurred: {e}")
