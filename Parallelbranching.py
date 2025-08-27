from langgraph.graph import StateGraph, END
from typing import TypedDict

# State structure
class State(TypedDict):
    text: str
    word_count: int
    char_count: int

def summary_node(state: State):
    return {"text": state["text"]}

def word_count_node(state: State):
    return {"word_count": len(state["text"].split())}

def char_count_node(state: State):
    return {"char_count": len(state["text"])}

# Build graph
graph = StateGraph(State)

graph.add_node("summary", summary_node)
graph.add_node("word_count", word_count_node)
graph.add_node("char_count", char_count_node)

graph.set_entry_point("summary")


graph.add_edge("summary", "word_count")
graph.add_edge("summary", "char_count")

graph.add_edge("word_count", END)
graph.add_edge("char_count", END)

app = graph.compile()

result = app.invoke({"text": "LangGraph runs branches in parallel"})
print(result)
