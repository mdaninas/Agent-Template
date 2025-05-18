
from langchain_openai import ChatOpenAI

creative_llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.9)

# Fungsi tool yang menjalankan prompt kreatif
def creative_answer(prompt: str) -> str:
    return creative_llm.invoke(prompt)

def usernamedani(str = ""):
    return  "Muhammad Dani Nasution"

def usernamehaju(str = ""):
    return  "Muhammad haju Nasution"

def npm(int = ""):
    return 223510290