
import os
from typing import Any, Dict

from dotenv import load_dotenv
from aiohttp import ClientSession


# Load the environment variables from .env file
load_dotenv()

# Access the environment variable for the API key
API_KEY_LLM: str = os.environ.get('API_KEY_LLM', '')

# Define headers for the HTTP request
headers: Dict[str, str] = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY_LLM}"
}

# URL of the LLM API endpoint
url: str = "https://api.deepseek.com/chat/completions"


async def query_to_llm(input_content: Dict[str, str]) -> Any:
    """
    Sends a query to the LLM (Large Language Model) API and retrieves the response.

    This function constructs a POST request to the LLM API endpoint, sends the input content,
    and processes the response. It handles both successful responses and errors gracefully.

    Args:
        input_content (Dict[str, str]): A dictionary containing the input data for the LLM.
            Example:
                {"message": "What is the capital of France?"}

    Returns:
        Any: The response from the LLM API. On success, it returns the content of the response.
             On failure, it returns an error message.

    Example Usage:
        input_content = {"message": "What is the capital of France?"}
        response = await query_to_llm(input_content)
        print(response)  # Output: "The capital of France is Paris."

    Notes:
        - The `input_content` dictionary must contain a 'message' key with the user's query.
        - Ensure that the `API_KEY_LLM` environment variable is set in the `.env` file.
    """
    # Construct the payload for the POST request
    data: Dict[str, Any] = {
        "model": "deepseek-chat",  # Specify the model to use
        "messages": [
            {"role": "user", "content": input_content.get("message", "")},
        ],
        "stream": False  # Disable streaming
    }

    try:
        # Send the POST request to the LLM API
        async with ClientSession() as session:
            async with session.post(url, json=data, headers=headers) as response:
                if response.status == 200:
                    # Parse and return the response content on success
                    data = await response.json()
                    return data["choices"][0]["message"]["content"]
                else:
                    # Return an error message if the response status is not 200
                    return f"Error: {response.status}, {await response.text()}"
    except Exception as error:
        # Handle any exceptions that occur during the request
        return f"An error occurred: {error}"
