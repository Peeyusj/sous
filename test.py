from app.graph.graph import app_graph

result = app_graph.invoke({"messages": [{"role": "user", "content": "what can I make with eggs and rice?"}], "image": "https://images.unsplash.com/photo-1617196030420-1e3f5c8b6f3e?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80"})
print(result)