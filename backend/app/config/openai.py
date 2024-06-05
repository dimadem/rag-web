from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

chat_model = ChatOpenAI(
    model="gpt-3.5-turbo-0125",
    temperature=0,
    api_key=os.environ["OPENAI_API_KEY"]
)