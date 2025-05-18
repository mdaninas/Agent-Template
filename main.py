from langchain_openai import ChatOpenAI
from langchain_core.tools import Tool
from langchain_core.prompts import PromptTemplate
from tools.tool import usernamedani, npm, usernamehaju, creative_answer
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub

llm = ChatOpenAI()

your_tools = [
    Tool.from_function(name="username1", func=usernamedani, description="Mengembalikan nama lengkap dani."),
    Tool.from_function(name="username2", func=usernamehaju, description="Mengembalikan nama lengkap haju."),
    Tool.from_function(name="creative", func=creative_answer, description="guankan hanya Jika tidak ada tool yang relevan / tidak dapat digunakan"),
    Tool.from_function(name="npm", func=npm, description="Mengembalikan NPM pengguna."),
]

template = """Jawablah pertanyaan berikut dengan menggunakan tools jika diperlukan:
{question}
kamu harus menjawab hanya denagn hasil return tool saja, tidak boleh ada tambahan kata
"""
prompt_template = PromptTemplate(template=template, input_variables=["question"])

react_prompt = hub.pull("hwchase17/react")

agent = create_react_agent(llm=llm, tools=your_tools, prompt=react_prompt)
executor = AgentExecutor(agent=agent, tools=your_tools, verbose=True)

def runbro(query):
    res = executor.invoke({"input": query})
    return res

if __name__ == "__main__":
    print("Hello from main")
    user_input = input("Masukkan Pertanyaan: ")
    result = runbro(user_input)
    print(result["output"])
