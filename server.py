import zmq
from prompts import generate_prompt

PORT = 5556

def create_success_response(prompt):
    """Create a successful JSON response."""

    return {
        "success": True,
        "prompt": prompt
    }


def create_error_response(error_message):
    """Create an error JSON response."""

    return {
        "success": False,
        "error": error_message
    }


def validate_request(request_data):
    """Validate incoming request data."""

    if not isinstance(request_data, dict):
        return False, "Request must be a JSON object."

    request_text = request_data.get("request")

    if request_text is None:
        return False, "Missing required field: request"

    if not isinstance(request_text, str):
        return False, "Field 'request' must be a string."

    if not request_text.strip():
        return False, "Field 'request' cannot be empty."

    return True, ""


def handle_request(request_data):
    """Validate the request and return a prompt or error response."""

    is_valid, error_message = validate_request(request_data)

    if not is_valid:
        return create_error_response(error_message)

    request_text = request_data["request"]
    details = request_data.get("details")

    prompt = generate_prompt(request_text, details)

    return create_success_response(prompt)


def main():
    """Start the ZeroMQ server and process prompt requests."""

    context = zmq.Context()
    socket = context.socket(zmq.REP)

    socket.bind(f"tcp://127.0.0.1:{PORT}")

    print(f"Prompts Microservice running on port {PORT}")

    while True:
        request_data = socket.recv_json()
        response = handle_request(request_data)
        socket.send_json(response)


if __name__ == "__main__":
    main()