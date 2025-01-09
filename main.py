# from langchain.document_loaders import HuggingFaceDatasetLoader
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain.embeddings import HuggingFaceEmbeddings
# from langchain.vectorstores import FAISS
# from transformers import AutoTokenizer, AutoModelForQuestionAnswering
# from transformers import AutoTokenizer, pipeline
# from langchain import HuggingFacePipeline
# from langchain.chains import RetrievalQA

# from langchain_community.chat_models import ChatOpenAI
# from langchain.chat_models.openai import ChatOpenAI
# from openai import OpenAI
from langchain_community.chat_models.gigachat import GigaChat
# from langchain_Giga ------------------------------------------------- 
from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.vectorstores import FAISS
from langchain.document_loaders import TextLoader
import os


os.environ['GIGACHAD_API_ACCESS_KEY'] = 'eyJjdHkiOiJqd3QiLCJlbmMiOiJBMjU2Q0JDLUhTNTEyIiwiYWxnIjoiUlNBLU9BRVAtMjU2In0.dAafB_JVjMoFSK7pwrsjNGp40NVZINCX_tphLmffBIGsgUC7qCFdH4qfp80sxUpRqNavRJoS-atZ6r4fdiD3kXTFszRp3VDdkBfULD8dBE3kfY39lN78gYRS8xlq_TCXkNeLpUTZX9uwsNO_Kyh9t9M21CuJswDMjthu-uzyeE4dQOoQSLO1ERZoCFHRrc_dynD82sxjVCdT1d1CGaQAKfqstPtde0CZOdf3IhfyZ_DgAT-QjDT6h1i8jme55nZZJfRe4tpNGYFgoWPB_-TUvdSlwCtr2M7Mcy_tXep0V1Tjg_4RyA8xDhHFI0-gMYeMVuVXpg0SYQ131HJh8d6iOQ.PmLNLNDXuDuNA1Lt8VoXyQ.pL6hjA0Hhk47rffqJZzeczU6UVQG6smZMkADrCvbCFHd86WQDW_UmwJ4OhcjxY0A3eUkKegNvIGbpuNJptgMf-83irxC51O91f7T-h22XmUFHg1bRYevv__Gms4lWhFXnl54RxxTAqliVdGl1baQjnWfV4RmMk5XpJV67olVmxnpLvNWbP1aAouaKk6FBm29Yy-EZep3nJsfkbOYCEfxUQ-dmPFUiYwB_R_JXOtUNFo6eWEw6zge0PcMnuyWDgjlUN98vdNuasylHru6C8AtH5LlZxNvnr5byR43BCoGVtKZANlCP5kxTBqJahuP-F3qOxD3RZOlnLcLRk3Z-BXWFyBQk6Tl9G89j2wH99IeMFGSk5QBZ3ZbkgmMxuufytUr7WUH5ZC1o4dVk_e6Jzm-fuljYmXNgEtbEyjNlX2Pk-Zkzp78T_ssKO9dsvLA7QDhEAh9170CpgNgcQyMQV7XZCH7xWGiNvQrap268kYWb8Cf6g9yA29Rbl0Tjzv2-rStyttVzNXNCorpXqefZ5bmMw306LyEbVK-nxyt7cxr1xhxFFkfp-khxstslPv8GuvnoxnTM2P0BUu3VWFg8DxO4fQPX_yVJVraSDKVo8wO7uPgSk_Ga66_-LbnHJC0-cpDQ9p7vTEoY3xpM2a70U9Zd-P_iIRzrPVRaamdlCN8IQFGih-OVpBX4-DdI2o7Lq4BuyVTFl-1XFo3xwy2eHLc-b4OydsfmfOGalBAybr9gVQ.JlgTBfDN7DuGa-EItVwdAvHHXP_zjKSsQb_IJn8pTEw'

# llm = GigaChat(model='Gigachad', temperature= .7)

# # Example dataset

# text_loader = TextLoader(file_path="test_file.txt")  # Replace with the path to your document file
# documents = text_loader.load()
# text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
# docs = text_splitter.split_documents(documents)

# texts = [doc.page_content for doc in docs]
# metadatas = [doc.metadata for doc in docs]

# embeddings = SentenceTransformerEmbeddings('all-MiniLM-L6-v2')

# doc_embeddings = embeddings.encode(texts)

# vector_store = FAISS.from_texts(docs, embedding=embeddings)

# vector_store.save_local('faiss_index')

# vector_store
# auth key : YjQyY2E5Y2ItZDYyOC00Mjc5LWJiNzEtZDFmYTgyMGUzZDYyOmRjMzA2ODdmLTJmMDUtNDEyZi1hOGM1LTY1OGZiZDQ5NzYzMw==

import requests

# url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"

# payload={
#   'scope': 'GIGACHAT_API_PERS'
# }
# headers = {
#   'Content-Type': 'application/x-www-form-urlencoded',
#   'Accept': 'application/json',
#   'RqUID': 'faa5785c-d4a1-4ad7-ac81-de35a899bd30',
#   'Authorization': 'Basic YjQyY2E5Y2ItZDYyOC00Mjc5LWJiNzEtZDFmYTgyMGUzZDYyOmRjMzA2ODdmLTJmMDUtNDEyZi1hOGM1LTY1OGZiZDQ5NzYzMw=='
# }

# response = requests.request("POST", url, headers=headers, data=payload)

# print(response.text)

url = "https://gigachat.devices.sberbank.ru/api/v1/models"

payload={}

headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer ' + os.environ['GIGACHAD_API_ACCESS_KEY']
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)



# access token:
# eyJjdHkiOiJqd3QiLCJlbmMiOiJBMjU2Q0JDLUhTNTEyIiwiYWxnIjoiUlNBLU9BRVAtMjU2In0.yhfkyF373T8qyYqm9j7WjWivDdR6nxu461mSbaVsFUMS9NXzwi9YVHId35bUKANlXD6cDlxZJmzS1sHQRWlzMwsGOl1yh_ZhCLDrduAX68hfHL2vzU73LlVNdZ9o6iLBrThxFFLtjlSpT81qAszN_UCwUpdf4B9GEnNJJC-r8hHAmBLoi-8xOtsNf5XzvRfx37kgtG7fSprr0j0Kvcq7gIa0HY5x377xEoNwXjStWgya1geiViXL3jqoocnTwsD9OIooZTaVumF1eqyIqVD6qDD5MlV9lcFJPQ7tO3-oHuiEUJTRpVfkDGtgCFaMKCZpbEsDmW1A-CUi7LEVXgNaZw.U6_GWxXY3tutQUJhaRSNmQ.OQJxa5hAWHS0Vg7goPfPma8qn8Zmx4E7VrefM5oqsDlYSpIWSRhXHVW5lHcLx38d0ywoRhgPvrECNuWIuOjJf6Aq4526Q_QAAJgaTAAjcXRaL1nOBQurMgeMH4yZIR_ncEHIOkfC8nm3-su6yEWgeGff8qjGkrIjXQOngPzoL_6Vk8-hdxrj5IPXpkWQZ4zmLa0K0_Rq6TELTTGKKRzXGS4F63yz5nzO6iDkz4eDSiELHa9CvXo5jI347hjzemBXAxtjzWESZWlqExUEloAkWFoeklHoOMmcpmWNPQ_EbeZIRB8t2Fn5poEYEJ5gKdTqAuJa1SQhF92DdIuF3EhL4PYIkRwNvcCLbCy-mWdZ__y5KaXA7Vn2FkaqJjSBtqW_Kbe-cf5Blk0C2MAve5Gz97mpuap0IZGfwlvyIJL2F7Z9HyjIONSEtltniIoF6p0AIukZ5lLhbLq_c4oGwil-shWhF2yHkhJKgK3mbhRUD66FFz2hUmIQaR0RRsjdAe5GZtV1Hz1gmV63GwKHX3B7DkFl-rxrFyu50aAUwf6PHcJ1e3cPz1RE6vIkLgzJblYk4hVT0vKZmGJA8SmiG0GmyinmFRbJAy2ICDmQjYbX9lh1vs5X9eFuKpBgiHgMR7w0VyEcBg1xdu9lX8w91w8pxxEv075jFJCA2o-Bd-LXNZHpDvA45Bj2fpDPNVgvQCsiKByF1FVAdasvr1q6h-ljpVewX26sg0zdHHsD84nVBOA.s9OdjYZa6Cn5hh_0Hjo3MLQ15oQzvB4iw9Ou1q5vc_8

