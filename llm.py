import os
from langchain.vectorstores import Chroma
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import TextLoader
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chat_models.gigachat import GigaChat
from langchain.chains import create_retrieval_chain

class LLM:
    def __init__(self):
        # Set up API key for GigaChat
        with open('api_key.txt', 'r') as f:
            key = f.read()

        os.environ['GIGACHAT_API_ACCESS_KEY'] = key

        # File paths to documents
        file_paths = [
            'docs/test.json',
            'docs/raw_recomm_papers_1.txt',
            'docs/raw_recomm_papers_2.txt',
            'docs/raw_recomm_papers_3.txt'
        ]

        # Load and split documents
        documents = []
        for file_path in file_paths:
            loader = TextLoader(file_path, encoding='utf-8')
            documents.extend(loader.load())

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
        docs = text_splitter.split_documents(documents)

        # Set up embeddings and vectorstore
        embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
        db = Chroma.from_documents(docs, embedding_function)
        retriever = db.as_retriever()

        # Set up LLM and chains
        llm = GigaChat(
            credentials=os.environ['GIGACHAT_API_ACCESS_KEY'],
            model="GigaChat",
            verify_ssl_certs=False,
            profanity_check=False,
        )

        self.llm = llm
        self.retriever = retriever
        

    def prompt(self):
        prompt = ChatPromptTemplate.from_template(''' Ты - консультант в техническом интернет-магазине \
                                                Ответь на вопрос пользователя. \
        Используй при этом информацию из контекста. Если в контексте нет \
        информации для ответа, попроси пользователя уточнить необходимые детали.
        Контекст: {context}
        Вопрос: {input}
        Ответ:''')

        document_chain = create_stuff_documents_chain(
            llm=self.llm,
            prompt=prompt,
        )

        retrieval_chain = create_retrieval_chain(self.retriever, document_chain)
        response = retrieval_chain.invoke({'input': user_input})
        return response
