from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, END
from langchain_groq import ChatGroq

# Step 1: Define state (what flows between nodes)
from typing import TypedDict

class State(TypedDict):
    question: str
    answer: str

def call_llm(state: State):
    # llm = ChatOpenAI(model="gpt-4o-mini", api_key="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")   # any model you want
    llm = ChatGroq(model="llama3-70b-8192", api_key="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")
    response = llm.invoke(state["question"])
    return {"answer": response.content}     # put result into state

# Step 3: Create graph
graph = StateGraph(State)

# Add nodes
graph.add_node("llm", call_llm)

graph.set_entry_point("llm")   # start with llm node
graph.add_edge("llm", END)     # go to END after llm

# Step 5: Compile graph
app = graph.compile()

# Step 6: Run it
result = app.invoke({"question": "What is LangGraph?"})
print(result)
