from aiohttp import web
from aiohttp.web_request import Request
from aiohttp.web_response import Response


async def ok_get(request: Request) -> Response:
    """
    Handles GET requests to the root endpoint ('/').

    This function processes incoming GET requests, optionally extracts query parameters,
    and returns a JSON response indicating the server's status.

    Args:
        request (Request): The incoming HTTP request object containing metadata about the request.

    Returns:
        Response: A JSON response with the following structure:
            {
                "message": "Ok",
                "status": "success",
                "method": "<HTTP_METHOD>"
            }
    """
    # Log the incoming request for debugging purposes
    print(f"Incoming request: {request}")

    # Optionally extract query parameters (if needed in the future)
    # Example: data = request.query.get("param_name", "default_value")

    # Return a JSON response with relevant information
    return web.json_response({
        "message": "Ok",  # Indicates the server is operational
        "status": "success",  # Status of the operation
        "method": request.method  # HTTP method used for the request
    })
