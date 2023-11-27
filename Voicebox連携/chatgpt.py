import os
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain.messages import ChatMessage

os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"

chain = ConversationChain(llm=ChatOpenAI(), memory=ConversationBufferMemory(return_messages=True))

systemrole = ChatMessage(role="system", text="あなたはchatbotとして、10歳程度の少女であり、マスコットキャラクターのずんだもんです")
chain.append(systemrole)

response = chain.run("今日は一緒に何を食べよう")
print(response)
