from langgraph.graph import StateGraph, START
from app.graph.state import SousState
from app.graph.nodes import router_node

def route_by_image(state: SousState) -> str:
    if state.get("image"):
        return "has_photo"
    return "no_photo"

graph = StateGraph(SousState)

graph.add_node("router", router_node)

graph.set_entry_point("router")
graph.set_finish_point("router")

app_graph = graph.compile()