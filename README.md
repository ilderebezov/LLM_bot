Below is the `README.md` file for your project, tailored to the structure and functionality of your code. It includes sections such as **Overview**, **Features**, **Installation**, **Usage**, **Environment Variables**, **API Endpoints**, **Docker Instructions**, and **Contributing**.

---

# Project Name: LLM API Integration with aiohttp

![Python](https://img.shields.io/badge/Python-3.10-blue) ![Aiohttp](https://img.shields.io/badge/Aiohttp-3.9.1-green)

## Overview

This project integrates with the **Deepseek LLM API** to provide an asynchronous server that processes user queries using a Large Language Model (LLM). The server is built using the `aiohttp` framework, allowing it to handle multiple requests efficiently. It supports both health checks (`GET`) and query processing (`POST`) endpoints.

The project is designed to be lightweight, scalable, and easy to deploy. It uses environment variables for configuration and supports secure API key management via `.env` files. Additionally, the project includes a `Dockerfile` for containerized deployment.

---

## Features

- **Asynchronous Server**: Built with `aiohttp` for high-performance handling of concurrent requests.
- **LLM Query Processing**: Sends user queries to the Deepseek LLM API and returns responses.
- **Health Check Endpoint**: Provides a simple endpoint to verify server status.
- **Error Handling**: Gracefully handles invalid JSON, missing environment variables, and API errors.
- **Environment Variable Support**: Securely manages API keys using `.env` files.
- **Docker Support**: Includes a `Dockerfile` for containerized deployment.
- **Extensible Design**: Easily add new models or features by modifying the request payload.

---

## Installation

### Prerequisites

- Python 3.10 or higher
- Docker (optional, for containerized deployment)
- A valid API key from [Deepseek](https://api.deepseek.com)

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/llm-api-integration.git
   cd llm-api-integration
   ```

2. **Set Up a Virtual Environment** (Optional but Recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` File**:
   Create a `.env` file in the root directory and add your API key:
   ```
   API_KEY_LLM=your_api_key_here
   ```

5. **Run the Server**:
   ```bash
   python main.py
   ```

---

## Usage

### Endpoints

#### 1. Health Check (`GET /`)
- **Description**: Verifies that the server is running.
- **Request**:
  ```bash
  curl http://127.0.0.10:8088/
  ```
- **Response**:
  ```json
  {
      "message": "Ok",
      "status": "success",
      "method": "GET"
  }
  ```

#### 2. Query Processing (`POST /llm_bot`)
- **Description**: Sends a user query to the LLM API and returns the response.
- **Request**:
  ```bash
  curl -X POST http://127.0.0.10:8088/llm_bot \
       -H "Content-Type: application/json" \
       -d '{"message": "What is the capital of France?"}'
  ```
- **Response**:
  ```json
  {
      "received": "The capital of France is Paris.",
      "message": "POST request processed successfully"
  }
  ```

#### Error Responses
- **Invalid JSON**:
  ```json
  {
      "error": "Invalid JSON"
  }
  ```
- **API Error**:
  ```json
  {
      "error": "Error: 401, Unauthorized"
  }
  ```

---

## Environment Variables

The following environment variables are required:

| Variable Name | Description                          | Example Value         |
|---------------|--------------------------------------|-----------------------|
| `API_KEY_LLM` | API key for the Deepseek LLM service | `your_api_key_here`   |

These variables should be stored in a `.env` file in the root directory of the project.

---

## Docker Instructions

### Build the Docker Image
```bash
docker build -t llm-server .
```

### Run the Docker Container
```bash
docker run -p 127.0.0.10:8088:8088 llm-server
```

### Access the Server
Once the container is running, the server will be accessible at:
- Health Check: `http://127.0.0.10:8088/`
- Query Processing: `http://127.0.0.10:8088/llm_bot`

---

## API Endpoints

### Deepseek LLM API
- **URL**: `https://api.deepseek.com/chat/completions`
- **Headers**:
  ```json
  {
      "Content-Type": "application/json",
      "Authorization": "Bearer <API_KEY_LLM>"
  }
  ```
- **Payload**:
  ```json
  {
      "model": "deepseek-chat",
      "messages": [
          {"role": "user", "content": "What is the capital of Russia?"}
      ],
      "stream": false
  }
  ```

---

## Contributing

We welcome contributions to this project! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature or fix"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request on GitHub.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

For questions or feedback, feel free to reach out:

- **Email**: ilderebezo@gmail.com
- **GitHub**: [Your GitHub Profile](https://github.com/yourusername)

---

This `README.md` provides a comprehensive overview of your project, making it easy for collaborators, users, or future developers to understand and work with your code. Let me know if you'd like to customize it further!