from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("huggingfacehub_api_token")
)

model = ChatHuggingFace(llm=llm)

response = model.invoke("Who is Yuvraj Singh?")
print(response.content)

