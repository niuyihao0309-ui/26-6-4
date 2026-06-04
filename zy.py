import time

import dotenv
import asyncio
from langchain_openai import ChatOpenAI
from langgraph.pregel.debug import tasks_w_writes
from watchfiles import awatch

dotenv.load_dotenv()

llm_tb=ChatOpenAI(model="deepseek-ai/DeepSeek-V4-Flash")


"""同步"""
# res = llm_tb.invoke("1+1等于几")
# print(res.content)

"""列表"""
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
response = llm_tb.invoke([
    SystemMessage(content="你是一个专业的Python编程助手"),
    HumanMessage(content="什么是装饰器？")
])
print(response.content)

"""多轮对话"""
conversation = [
    HumanMessage(content="什么是LangChain？"),
    AIMessage(content="LangChain是一个用于开发大模型应用的框架。"),
    HumanMessage(content="它有哪些核心组件？")  # 这依赖于上一轮的上下文
]

response = llm_tb.invoke(conversation)
print(response.content)


"""元组，字典"""
tuple_messages = [
    ("system", "你是一个专业的Python编程助手"),
    ("user", "什么是装饰器？")
]

# 字典方式：{"role": 角色, "content": 内容}
dict_messages = [
    {"role": "system", "content": "你是一个专业的Python编程助手"},
    {"role": "user", "content": "什么是装饰器？"}
]

print(llm_tb.invoke(tuple_messages))
print(llm_tb.invoke(dict_messages))




"""异步"""
# async def main():
#     llm_yb = ChatOpenAI(
#         model="deepseek-ai/DeepSeek-V4-Flash",
#     )
#     res = await llm_yb.ainvoke("1+1等于几")
#     print(res.content)
#
# if __name__ == "__main__":
#     asyncio.run(main())
"""异步"""
# import asyncio
# from dotenv import load_dotenv
# from langchain_openai import ChatOpenAI
#
# load_dotenv()
# llm = ChatOpenAI(model="deepseek-ai/DeepSeek-V4-Flash")
#
# async def right_way():
#     tasks = [
#         llm.ainvoke("1+1等于几"),       # 创建协程，但不等待
#         llm.ainvoke("2+2等于几"),       # 创建协程，但不等待
#         llm.ainvoke("3+3等于几"),       # 创建协程，但不等待
#     ]
#     r1, r2, r3 = await asyncio.gather(*tasks)  # 三个请求同时发出，同时等待
#     print("1+1 :", r1.content)
#     print("2+2 :", r2.content)
#     print("3+3 :", r3.content)
#
# if __name__ == "__main__":
#     asyncio.run(right_way())


"""同步异步对比"""
# import time
# import asyncio
# from langchain_openai import ChatOpenAI
# # dotenv.load_dotenv()
#
# llm_tb=ChatOpenAI(model="deepseek-ai/DeepSeek-V4-Flash")
# prompts = ["用一句话介绍一下北京",
#     "用一句话介绍一下上海",
#     "用一句话介绍一下广州"]
#
# print("-"*5,"同步","-"*5)
# def text1():
#     start = time.time()
#     for i,prompt in enumerate(prompts):
#         print(f"发送第{i + 1}个请求")
#         result = llm_tb.invoke(prompt)
#         print(f"第{i + 1}个结果：{result.content}")
#     print(f"总时间：{time.time() - start}\n")
#     print("-"*5,"异步","-"*5)
# async def text2():
#     start2 = time.time()
#     tasks = [llm_tb.ainvoke(prompt) for prompt in prompts]
#     results = await asyncio.gather(*tasks)
#
#     for i, result in enumerate(results):
#         print(f"第{i + 1}个结果：{result.content}")
#
#     print(f"总时间{time.time() - start2}\n")
#
# async def text3():
#     text1()
#     await  text2()
# if __name__ == "__main__":
#     asyncio.run(text3())


"""流动输出"""
# def str1():
#     from langchain_openai import ChatOpenAI
#     llm_ss = ChatOpenAI(model="deepseek-ai/DeepSeek-V4-Flash")
#     print("AI...回答")
#     full_message = None     # 创建一个空的"笔记本"
#     for chunk in llm_ss.stream("写一首超简单的古诗"):    # stream -- 流动显示（增加用户体验感）
#         full_message = chunk if full_message is None else full_message + chunk
#         time.sleep(0.1)
#         print(chunk.content, end="",flush=True)
#
#
#     print(f"\n\n 完整信息：\n{full_message.content}")
#
# str1()

































