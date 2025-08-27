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
def explain(state: State):
    llm = ChatGroq(model="llama3-70b-8192", api_key="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")
    response = llm.invoke("Explain in detail: " + state["answer"])
    return {"answer": response.content}
def router(state: State):
    if "summarize" in state["question"].lower():
        return "summarize"
    elif "points" in state["question"].lower():
        return "makeaspoints"
    else:
        return "explain"   
    

graph.add_node("llm",call_llm)
graph.add_node("summarize",summarize)
graph.add_node("makeaspoints",makeaspoints)
graph.add_node("explain",explain)




graph.set_entry_point("llm")



graph.add_conditional_edges("llm", router,{
    "summarize": "summarize",
    "makeaspoints": "makeaspoints",
    "explain": "explain"
})
graph.add_edge("summarize",END)
graph.add_edge("makeaspoints",END)
graph.add_edge("explain",END)

app=graph.compile()
result=app.invoke({"question":"Summarize about langraph?"})
print(result)
