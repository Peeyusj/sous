from langgraph.graph import StateGraph, END
from app.graph.state import SousState
from app.graph.nodes import router_node

graph = StateGraph(SousState)

graph.add_node("router", router_node)

graph.set_entry_point("router")
graph.set_finish_point("router")

app_graph = graph.compile()