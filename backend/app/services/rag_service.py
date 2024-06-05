from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

# Инициализация модели OpenAI
chat_model = ChatOpenAI(
    model="gpt-3.5-turbo-0125",
    temperature=0,
    api_key=os.environ["OPENAI_API_KEY"]
)

# Шаблон для RAG
rag_prompt = ChatPromptTemplate.from_messages([
    ("system", 'You are a helpful assistant. Use the following context when responding:\n\n{context}.'),
    ("human", "{question}")
])

# Цепочка RAG
rag_chain = rag_prompt | chat_model | StrOutputParser()

def process_question(question, context):
    if context is None:
        context = """
        Old Ship Saloon 2023 quarterly revenue numbers:
        Q1: $174782.38
        Q2: $467372.38
        Q3: $474773.38
        """
    
    response = rag_chain.invoke({
        "question": question,
        "context": context
    })
    
    return response