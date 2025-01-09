from llm import LLM

# def 
llm = LLM()

llm.set_prompt()

question = "Какой лучше ноутбук подойдёт для пожилого человека на пенсии, который любит смотреть разные фильмы, но которые не показывают по телевизору?"

response = llm.invoke(question)

print(response['answer'])

