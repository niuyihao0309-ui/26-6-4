
# 统一接口的价值
# 不管你用的是 OpenAI、DeepSeek、Claude 还是本地的 Ollama，LangChain 都提供了完全一致的调用方式：

# import os
# import dotenv
# from langchain_openai import ChatOpenAI
# dotenv.load_dotenv()
# llm_ds=ChatOpenAI(
#     model="deepseek-ai/DeepSeek-V4-Flash",
#     api_key=os.getenv("OPENAI_API_KEY"),
#     base_url=os.getenv("OPENAI_BASE_URL")
# )
# response = llm_ds.invoke("用一句话介绍自己")
# print(response.content)

# 同步 invoke
# 异步 asyncio


#   --- 异步函数---异步输出---
# # 1. 导入需要的库
# import asyncio  # Python自带的异步标准库
# from dotenv import load_dotenv  # 加载.env环境变量
# from langchain_openai import ChatOpenAI  # LangChain的OpenAI对话模型
# # 2. 加载.env文件里的OPENAI_API_KEY（必须先在项目根目录创建.env文件）
# load_dotenv()
# # 3. 初始化ChatOpenAI模型（和同步写法完全一样）
# llm = ChatOpenAI(model="deepseek-ai/DeepSeek-V4-Flash", temperature=0.7)  #温度
# # 4. 定义异步函数（所有带await的代码必须放在async def里面）
# async def main():
#     # ------------------- 用法1：一次性异步调用（等全部结果返回） -------------------
#     print("=== 一次性异步调用 ===")
#     # await = "等这个异步操作完成再往下走"
#     # ainvoke = 异步版的invoke（所有LangChain异步方法都以a开头）
#     response = await llm.ainvoke("用一句话介绍Python")
#     print("回答：", response.content)
#     print("-" * 50)
#
#     # ------------------- 用法2：异步流式输出（打字机效果，最常用） -------------------
#     print("\n=== 异步流式输出（打字机效果） ===")
#     # astream = 异步版的stream，逐字返回结果
#     async for chunk in llm.astream("用3句话介绍人工智能"):
#         # 每次打印一个字块，不换行
#         print(chunk.content, end="", flush=True)
#     print("\n" + "-" * 50)
#
# # 5. 运行异步函数（Python异步程序的标准入口）
# if __name__ == "__main__":
#     asyncio.run(main())

""""
对话型，用户提问
用户消息--HumanMessage	--用户的输入:"llm.invoke([HumanMessage(content="你好")])"
"""""

# from langchain_core.messages import (
#     HumanMessage
# )
# from langchain_openai import ChatOpenAI
#
# llm = ChatOpenAI(model="deepseek-ai/DeepSeek-V4-Flash")

# 单个消息
# response = llm.invoke([HumanMessage(content="你好")])
# print(response.content)



"""""
与AI长聊天对话
"""
# from langchain_openai import ChatOpenAI
# llm = ChatOpenAI(model="deepseek-ai/DeepSeek-V4-Flash")
# from langchain_core.messages import (
#     HumanMessage,SystemMessage,AIMessage
# )
# # 对话历史——模拟多轮对话
# conversation = [
#     SystemMessage(content="你是一个有帮助的AI助手"),           # 系统消息 -- AI人设     设定AI的"人设"和行为规则
#     HumanMessage(content="你好，我叫hzk"),                   # 用户消息
#     AIMessage(content="你好！hzk,有什么我可以帮助你的吗？"),     # AI消息
#     HumanMessage(content="我叫什么名字？"),                   # 用户消息
#     ]
#
# response = llm.invoke(conversation)
# print(response.content)

""""
# await call_llm_async() # 方式一                  # 只能在async def异步函数内部
# asyncio.run(call_llm_async()) # 方式二           # 只能在同步代码（全局 / 普通函数）中

异步
"""
# import asyncio
# from dotenv import load_dotenv
# from langchain_openai import ChatOpenAI
#
# load_dotenv()
# llm = ChatOpenAI(model="deepseek-ai/DeepSeek-V4-Flash")
#
#
# # 定义一个异步函数（里面才能用await）
# async def call_llm_async(prompt):
#     response = await llm.ainvoke(prompt)
#     return response.content
#
#
# # ------------------- 正确用法 -------------------
# async def main():
#     # ✅ 正确：在异步函数内部用await
#     result1 = await call_llm_async("1+1等于几")
#     print("结果1：", result1)
#
#     # ✅ 正确：一个异步函数里可以有多个await
#     result2 = await call_llm_async("2+2等于几")
#     print("结果2：", result2)
#
#
# # ✅ 正确：在全局同步代码中用asyncio.run启动
# if __name__ == "__main__":
#     final_result = asyncio.run(main())
#     print("程序最终返回：", final_result)      # 返回None

    # 你的 main() 异步函数没有写 return 语句 **，Python 中所有函数（包括异步函数）默认都会返回 None。
    # asyncio.run() 只是忠实地把 main() 函数最终返回的结果原封不动地传给你，所以你得到了 None


# ------------------- 错误用法 -------------------
# ❌ 错误：不能在全局同步代码中直接用await
# result = await call_llm_async("3+3等于几")  # 会报SyntaxError

# ❌ 错误：不能在异步函数内部用asyncio.run
# async def bad_demo():
#     asyncio.run(call_llm_async("4+4等于几"))  # 会报RuntimeError



"""
ainvoke 负责"能让出"，gather 负责"同时跑
ainvoke() 解决的是 → "等待时不阻塞"（让出 CPU，别的任务有机会插进来）
gather()  解决的是 → "同时派发多个任务"（把多个协程塞进事件循环并行跑）
"""
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
#     # 总耗时：~2秒（并行）
#     print("1+1 :", r1.content)
#     print("2+2 :", r2.content)
#     print("3+3 :", r3.content)
#
#
# # ✅ 关键：启动异步事件循环，执行right_way()函数
# if __name__ == "__main__":
#     asyncio.run(right_way())



"""
ainvoke，asyncio，gather       什么意思什么区别
"""
# asyncio：Python 自带的整个异步编程的操作系统 / 平台，没有它所有异步代码都跑不起来
# ainvoke：LangChain 提供的单个异步任务（相当于 "点一份外卖"）----它是LangChain 专属的异步方法 , 只能说明是异步处理不能进行运行
# asyncio.gather()：asyncio平台提供的批量任务管理器（相当于 "同时点 10 份外卖，一起等送到"）--- 1.接收多个协程对象（多个外卖订单）
#                                                                                   2.把它们全部提交给事件循环，同时开始执行
#                                                                                   3.等待所有任务都完成，然后按传入顺序返回所有结果




# from dotenv import load_dotenv
# load_dotenv()
# def streaming_example():
#     from langchain_openai import ChatOpenAI
#     llm = ChatOpenAI(model="deepseek-ai/DeepSeek-V4-Flash")
#
#     print("AI回答: ")
#     full_message = None     # 创建一个空的"笔记本"
#     for chunk in llm.stream("请写一首关于春天的诗"):  # stream -- 流动显示（增加用户体验感）
#         # 累积消息块
#         full_message = chunk if full_message is None else full_message + chunk      # 把AI的文字一个一个的存入"笔记本"
#         print(chunk.content, end="", flush=True)  # 流动输出  # 强制立刻打印。有时候程序会把输出攒起来一起显示，加这个就能保证 AI 每输出一个字，你立刻就能看到，不会卡顿
#
#     # 完整消息
#     print(f"\n\n完整消息:\n{full_message.content}")
#
# streaming_example()  # 调用上方函数








