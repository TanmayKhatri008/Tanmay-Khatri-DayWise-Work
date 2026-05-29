from dotenv import load_dotenv

load_dotenv()

from typing import TypedDict
from typing import List
from typing import Optional
from typing import Annotated

import operator

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage
from langchain_core.messages import AIMessage

from langgraph.graph import StateGraph
from langgraph.graph import START
from langgraph.graph import END

from ingest.ingest import build_vectorstore

vectorstore = build_vectorstore()

retriever = vectorstore.as_retriever(search_kwargs={"k": 3})


class AgentState(TypedDict):
    messages: Annotated[List, operator.add]
    retrieved_chunks: Optional[List[str]]
    needs_retrieval: Optional[bool]


llm = ChatMistralAI(model="mistral-large-latest", temperature=0)


def agent_node(state):

    question = state["messages"][-1].content

    prompt = f"""
Question: {question}

Do you need documents to answer this?

Reply only YES or NO.
"""

    response = llm.invoke([HumanMessage(content=prompt)])

    answer = response.content.strip()

    return {"needs_retrieval": answer.upper() == "YES"}


def retrieve_node(state):

    question = state["messages"][-1].content

    docs = retriever.invoke(question)

    chunks = []

    for doc in docs:

        source = doc.metadata.get("source", "unknown")

        chunk_number = doc.metadata.get("chunk_index", "?")

        text = f"[{source} chunk {chunk_number}] " f"{doc.page_content}"

        chunks.append(text)

    return {"retrieved_chunks": chunks}


def answer_node(state):

    question = state["messages"][-1].content

    chunks = state.get("retrieved_chunks") or []

    context = "\n\n".join(chunks)

    if context:

        prompt = f"""
Answer using only the context below.

Context:
{context}

Question:
{question}
"""

    else:
        prompt = question

    response = llm.invoke([HumanMessage(content=prompt)])

    return {"messages": [AIMessage(content=response.content)]}


def route(state):

    if state.get("needs_retrieval"):
        return "retrieve"

    return "answer"


builder = StateGraph(AgentState)

builder.add_node("agent", agent_node)

builder.add_node("retrieve", retrieve_node)

builder.add_node("answer", answer_node)

builder.add_edge(START, "agent")

builder.add_conditional_edges("agent", route)

builder.add_edge("retrieve", "answer")

builder.add_edge("answer", END)

graph = builder.compile()
