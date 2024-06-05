from flask import Flask, request, jsonify
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

chat_model = ChatOpenAI(
    model="gpt-3.5-turbo-0125",
    temperature=0,
    api_key=os.environ["OPENAI_API_KEY"]
)

SOURCE = """
Old Ship Saloon 2023 quarterly revenue numbers:
Q1: $174782.38
Q2: $467372.38
Q3: $474773.38
"""

rag_prompt = ChatPromptTemplate.from_messages([
    ("system", 'You are a helpful assistant. Use the following context when responding:\n\n{context}.'),
    ("human", "{question}")
])

rag_chain = rag_prompt | chat_model | StrOutputParser()

@app.route('/api/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get('question')
    context = data.get('context', SOURCE)
    
    response = rag_chain.invoke({
        "question": question,
        "context": context
    })
    
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
