import json
from typing import Any

from aiohttp import web
from aiohttp.web_request import Request
from aiohttp.web_response import Response

from src.llm_requests.llm_req import query_to_llm


async def llm_post(request: Request) -> Response:
    """
    Handles POST requests to the '/llm_bot' endpoint.

    This function processes incoming POST requests, extracts JSON data, sends it to an LLM (Large Language Model)
    via the `query_to_llm` function, and returns a JSON response with the results.

    Args:
        request (Request): The incoming HTTP request object containing POST data.

    Returns:
        Response: A JSON response with one of the following structures:
            - On success:
                {
                    "received": <response_from_llm>,
                    "message": "POST request processed successfully"
                }
            - On failure (invalid JSON):
                {
                    "error": "Invalid JSON"
                }

    Raises:
        json.JSONDecodeError: If the incoming request contains invalid JSON data.
    """
    try:
        # Extract JSON data from the POST request
        data_request: dict = await request.json()

        # Query the LLM with the extracted data
        response_from_llm: Any = await query_to_llm(input_content=data_request)

        # Construct the response
        response = {
            "received": response_from_llm,
            "message": "POST request processed successfully"
        }
        return web.json_response(response, status=200)

    except json.JSONDecodeError:
        # Handle cases where the request body contains invalid JSON
        return web.json_response({"error": "Invalid JSON"}, status=400)

