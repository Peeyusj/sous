from langchain_ollama import ChatOllama

from app.graph.state import SousState

def router_node(state: SousState) -> dict:
    llm = ChatOllama(model="qwen2.5:3b")
    last_message = state["messages"][-1]["content"]

    reply = llm.invoke(last_message)

    new_messages = state["messages"] + [{"role": "assistant", "content": reply.content}]
    return {"messages": new_messages}