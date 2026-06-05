""""
机试题1
"""
from click import prompt

# from langchain_core.callbacks import get_usage_metadata_callback
# from langchain_openai import ChatOpenAI
#
# llm = ChatOpenAI(model="deepseek-ai/DeepSeek-V4-Flash")
#
# with get_usage_metadata_callback() as cb:
#     llm.invoke("写一首超级简单的歌曲")
#     res = llm.invoke("写一首超级简单的歌曲")
#     print(res.content)
#     print(cb.usage_metadata)


"""'
机试题二
"""
# from langchain_core.callbacks import get_usage_metadata_callback
# from langchain_openai import ChatOpenAI
#
# llm = ChatOpenAI(model="deepseek-ai/DeepSeek-V4-Flash")
# text2 = [
#         "1+1等于几",
#         "2+2等于几",
#         "3+3等于几"
#     ]
# with get_usage_metadata_callback() as cd:
#     res = llm.batch(text2)
#
#     for i, (question, res) in enumerate(zip(text2, res), 1):
#         print(f"第 {i} 个问题:{question}")
#         print(f"回答：{res.content}\n")
#
# print(cd.usage_metadata)


"""
机试题三
"""
from langchain_core.prompts import ChatPromptTemplate,HumanMessagePromptTemplate,MessagesPlaceholder
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.callbacks import get_usage_metadata_callback
from langchain_openai import ChatOpenAI
promtss = ChatPromptTemplate.from_messages([
    ("system","你是一个优秀的感情专家"),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])
llm = ChatOpenAI(model="deepseek-ai/DeepSeek-V4-Flash")
message1 = {
    "history":[
        HumanMessage(content="我好难过"),
        AIMessage(content="能体会到你的难过，但是你可以给我讲一下吗")
    ],
    "input":"我把杯子打碎啦"
}


with get_usage_metadata_callback() as cm:
    res = llm.batch(message1)

print(cm.usage_metadata)
print(message1)




















