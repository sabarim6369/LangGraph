from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, END
from typing import TypedDict
class State(TypedDict):
    question: str
    answer: str
graph=StateGraph(State)
def call_llm(state: State):
    llm=ChatGroq(model="llama3-70b-8192",api_key="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")
    response=llm.invoke(state["question"])
    return{"answer":response.content}
def summarize(state:State):
    llm=ChatGroq(model="llama3-70b-8192",api_key="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")
    response=llm.invoke("Summarize this:"+state["answer"])
    return{"answer":response.content}
def makeaspoints(state:State):
    llm=ChatGroq(model="llama3-70b-8192",api_key="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")
    response=llm.invoke("Make this into points:"+state["answer"])
    return{"answer":response.content}

graph.add_node("llm",call_llm)
graph.add_node("summarize",summarize)
graph.add_node("makeaspoints",makeaspoints)
graph.set_entry_point("llm")
graph.add_edge("llm","summarize")
graph.add_edge("summarize","makeaspoints")
graph.add_edge("makeaspoints",END)
app=graph.compile()
result=app.invoke({"question":"What is LangGraph?"})
print(result)
