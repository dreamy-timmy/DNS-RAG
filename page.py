from llm import LLM
import streamlit as st
# Streamlit application
st.title("Консультант по ноутбукам")
st.write("Задайте вопрос")

# Initialize LLM
llm_instance = LLM()

# User input
user_input = st.text_input("Введите ваш вопрос:")

if st.button("Получить ответ"):
    if user_input:
        with st.spinner("Генерируем ответ..."):
            try:
                response = llm_instance.prompt(user_input)
                st.success("Ответ готов!")
                st.write(response)
            except Exception as e:
                st.error(f"Ошибка: {str(e)}")
    else:
        st.warning("Введите вопрос перед поиском ответа.")
    