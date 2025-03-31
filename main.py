from fastapi import FastAPI
from fastapi_mcp import add_mcp_server
from fastapi.middleware.cors import CORSMiddleware

import mcp_client_api

# Your FastAPI app
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (change for production)
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

# Mount the MCP server to your app
mcp_server = add_mcp_server(
    app,                    # Your FastAPI app
    mount_path="/mcp",      # Where to mount the MCP server
    name="My API MCP",      # Name for the MCP server
)

@mcp_server.tool()
def add_numbers(x: int, y: int) -> int:
    return x + y

@mcp_server.tool()
def substract_numbers(x: int, y: int) -> int:
    return x - y

@mcp_server.tool()
def multiply_numbers(x: int, y: int) -> int:
    return x * y


app.include_router(mcp_client_api.route, prefix="/client", tags=["mcp"])

# Run the server if this file is executed directly
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8002)