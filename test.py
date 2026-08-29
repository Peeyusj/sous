from app.graph.graph import app_graph

result = app_graph.invoke({"messages": [{"role": "user", "content": "what can I make with eggs and rice?"}]})
print(result)