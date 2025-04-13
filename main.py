# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple some-package


from aiohttp import web

# Importing handler functions for GET and POST requests
from src.handles_post.llm_post_handle import llm_post  # Handles POST requests for '/llm_bot'
from src.handles_get.get_ok_handle import ok_get  # Handles GET requests for '/'

# Create the aiohttp application
app = web.Application()

# Add routes for handling GET and POST requests
app.router.add_get("/", ok_get)  # Route for health check or simple response
app.add_routes([web.post('/llm_bot', llm_post)])  # Route for processing POST requests to '/llm_bot'


def run_server() -> None:
    """
    Starts the aiohttp server.

    This function initializes and runs the server on the specified host and port.
    The server listens for incoming HTTP requests and routes them to the appropriate handlers.

    Configuration:
    - Host: '0.0.0.0' (Listens on all available network interfaces)
    - Port: 8080 (Standard HTTP port for the server)

    Note:
    - Setting `host='0.0.0.0'` allows the server to accept connections from external clients.
    - Ensure port `8080` is open and not blocked by firewalls if exposing the server externally.

    Returns:
        None
    """
    web.run_app(app, host='127.0.0.10', port=8088)


if __name__ == '__main__':
    """
    Entry point of the application.

    When this script is executed directly, it calls the `run_server` function
    to start the aiohttp server.
    """
    run_server()
