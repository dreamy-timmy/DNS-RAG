import streamlit as st

import sys
import os

# Добавить корневую директорию в sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")

from model.llm import LLM
llm = LLM()
llm.set_prompt()



st.title("💬 Чатбот-консультант ноутбуков")
st.caption("Ваш помощник по выбору ноутбука на все случаи жизни")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Доброго времени суток! Как я могу помочь?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])
    
if question := st.chat_input('Введите запрос:'):
    #llm_instance = LLM()
    st.session_state.messages.append({"role": "user", "content": question})
    st.chat_message("user").write(question)
    response = llm.invoke(question)['answer'] #llm_instance.prompt(prompt)  
    msg = 'Ответ'#response. ?
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.chat_message("assistant").markdown(response)
