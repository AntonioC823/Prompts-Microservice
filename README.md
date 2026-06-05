Prompts-Microservice

The Prompts Microservice generates customized prompts using Google's Gemini AI and returns them as JSON responses. Applications can send a request containing instructions for the AI along with optional details. The microservice will respond with either a generated prompt or an error message.

Before running the microservice, users must create a free Gemini API key. Please note that the free tier currently allows up to 20 requests per day.
If the API key is not configured correctly, the microservice will be unable to generate prompts.
Visit https://aistudio.google.com
Sign in with a Google account.
Select Get API Key.
Create a new API key.
Open a PowerShell terminal and set the environment variable (this helps prevent accidentally exposing your API key in source code or GitHub repositories):
$env:GEMINI_API_KEY="YOUR_API_KEY_HERE"

To programmatically REQUEST data from the microservice:

A program connects to it using ZeroMQ. It sends a message in JSON format that includes the required information:

request: Instructions describing the prompt the AI should generate.
details: Optional contextual information used to customize the generated prompt.

The service returns an error message if:

request is missing
request is not a string
request is an empty string

Example Error Response:

{
    "success": false,
    "error": "Missing required field: request"
}

Example Request Code:

import zmq

# Create a ZeroMQ context and request socket
context = zmq.Context()
socket = context.socket(zmq.REQ)

# Connect to the prompts microservice
socket.connect("tcp://localhost:5556")

# Build request message
request = {
    "request": "Generate a story prompt for this character and world.",
    "details": {
        "character_name": "Aric",
        "character_class": "Warrior",
        "world_name": "Eldoria"
    }
}

socket.send_json(request)

Explanation:

ZeroMQ context and REQ socket are created.
The client connects to the microservice at tcp://localhost:5556.
JSON request is constructed with the required fields.
The request is sent to the microservice.

To programmatically RECEIVE data from the microservice:

After sending a request, the program waits for a response from the microservice. The response comes back as a JSON object.

Example Response Code:

response = socket.recv_json()

print(response)

Example Successful Response:

{
    "success": true,
    "prompt": "Generate a story about a warrior named Aric exploring the world of Eldoria..."
}

Response Fields:

success: Indicates whether the request was processed successfully.
prompt: The AI-generated prompt returned by the microservice.

Example Error Response:

{
    "success": false,
    "error": "Field 'request' cannot be empty."
}