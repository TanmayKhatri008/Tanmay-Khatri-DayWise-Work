from dotenv import load_dotenv
from typing import TypedDict, Annotated

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages

from langchain_core.messages import HumanMessage, AIMessage, ToolMessage

from langchain_core.tools import tool

from langchain_mistralai import ChatMistralAI

load_dotenv()


llm = ChatMistralAI(model="mistral-large-latest", temperature=0)


@tool
def calculator(expression: str) -> str:
    """
    Evaluate a math expression.
    """

    try:
        result = eval(expression)
        return f"Result: {result}"

    except Exception as e:
        return f"Error: {str(e)}"


@tool
def search(query: str) -> str:
    """
    Fake search tool.
    """

    database = {
        "population of japan": "125 million",
        "capital of india": "New Delhi",
        "largest planet": "Jupiter",
        "president of usa": "Depends on current year",
    }

    return database.get(query.lower(), "No result found")


tools = [calculator, search]
tool_map = {"calculator": calculator, "search": search}


llm_with_tools = llm.bind_tools(tools)


class GraphState(TypedDict):
    messages: Annotated[list, add_messages]


def agent_node(state: GraphState):
    messages = state["messages"]
    response = llm_with_tools.invoke(messages)
    return {"messages": [response]}


def tool_node(state: GraphState):
    messages = state["messages"]
    last_message = messages[-1]
    tool_messages = []
    if not isinstance(last_message, AIMessage):
        return state

    if not last_message.tool_calls:
        return state
    for tool_call in last_message.tool_calls:

        tool_name = tool_call["name"]
        tool_args = tool_call["args"]
        tool_id = tool_call["id"]
        tool_function = tool_map[tool_name]
        result = tool_function.invoke(tool_args)
        tool_message = ToolMessage(content=str(result), tool_call_id=tool_id)
        tool_messages.append(tool_message)

    return {"messages": tool_messages}


def reflection_node(state: GraphState):
    messages = state["messages"]
    last_message = messages[-1]
    reflection_prompt = f"""
    Check if this answer is correct.
    Answer:
    {last_message.content}
    If wrong -> say RETRY
    If correct -> say FINISH
    """
    response = llm.invoke(reflection_prompt)
    return {"messages": [AIMessage(content=response.content)]}


def should_continue(state: GraphState):
    messages = state["messages"]
    last_message = messages[-1]
    if hasattr(last_message, "tool_calls") and last_message.tool_calls:
        return "tools"

    return "reflect"


def reflection_router(state: GraphState):
    messages = state["messages"]
    last_message = messages[-1]
    content = last_message.content.upper()
    if "RETRY" in content:
        return "agent"
    return END


graph_builder = StateGraph(GraphState)


graph_builder.add_node("agent", agent_node)
graph_builder.add_node("tools", tool_node)
graph_builder.add_node("reflect", reflection_node)

graph_builder.add_edge(START, "agent")

graph_builder.add_conditional_edges(
    "agent", should_continue, {"tools": "tools", "reflect": "reflect"}
)

graph_builder.add_edge("tools", "agent")
graph_builder.add_conditional_edges(
    "reflect", reflection_router, {"agent": "agent", END: END}
)

graph = graph_builder.compile()

while True:

    user_input = input("\nYou: ")
    if user_input.lower() == "exit":
        break

    result = graph.invoke({"messages": [HumanMessage(content=user_input)]})
    print("\n================ RESULT ================\n")
    for message in result["messages"]:

        print(f"{message.__class__.__name__}:")
        print(message.content)
        print()