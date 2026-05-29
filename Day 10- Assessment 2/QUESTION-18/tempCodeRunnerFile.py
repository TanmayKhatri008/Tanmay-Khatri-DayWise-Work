from agent.agent import graph
from langchain_core.messages import HumanMessage

while True:
    question = input("\nAsk a question: ")

    if question.lower() == "exit":
        break

    result = graph.invoke({"messages": [HumanMessage(content=question)]})

    print("\nAnswer:")
    print(result["messages"][-1].content)
