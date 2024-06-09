from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
from app.services.search_service import search_and_parse
from app.services.wikipedia_service import search_wiki

chat_model = ChatOpenAI(
    model="gpt-4o",
    max_tokens=4000,
    temperature=0,
    api_key=os.environ["OPENAI_API_KEY"]
)

rag_prompt = ChatPromptTemplate.from_messages([
    ("system", 'You are a helpful assistant from Wikipedia. Use the only following context when responding:\n\n{context}. If there no context, just tell that you dont know.'),
    ("user", "{question}")
])

rag_chain = rag_prompt | chat_model | StrOutputParser()



def process_question(question, context):
    data = search_wiki(question)
    if context is None:
        context = data
        print(f"context->\n", context)
    response = rag_chain.invoke({
        "question": question,
        "context": context
    })
    return response
