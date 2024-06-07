from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
from app.services.search_service import search_and_parse
from app.services.buffer.utils import clear_buffer

chat_model = ChatOpenAI(
    model="gpt-4o",
    max_tokens=4000,
    temperature=0,
    api_key=os.environ["OPENAI_API_KEY"]
)

rag_prompt = ChatPromptTemplate.from_messages([
    ("system", 'You are a helpful assistant. Use the following context when responding:\n\n{context}.'),
    ("user", "{question}")
])

rag_chain = rag_prompt | chat_model | StrOutputParser()



def process_question(question, context):
    data_from_web = search_and_parse(question)
    if context is None:
        context = data_from_web
        print("context->>>> ", context)
    response = rag_chain.invoke({
        "question": question,
        "context": context
    })
    return response
