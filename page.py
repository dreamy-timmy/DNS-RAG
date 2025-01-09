from llm import LLM
import streamlit as st

st.title("💬 Чатбот-консультант")
st.caption("Ваш помощник по выбору ноутбука на все случаи жизни")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Доброго времени суток! Как я могу помочь?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])
    
if prompt := st.chat_input('Введите запрос:'):
    #llm_instance = LLM()
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = ''#llm_instance.prompt(user_input)  
    msg = 'Ответ'#response. ?
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
