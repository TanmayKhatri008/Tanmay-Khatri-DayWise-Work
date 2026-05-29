from mcp.server import Server
from mcp.server.stdio import stdio_server

import asyncio

server = Server("calculator")


@server.tool()
async def calculate(expression: str):
    try:
        result = eval(expression, {"__builtins__": {}}, {})

        return str(result)

    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    asyncio.run(stdio_server(server))
