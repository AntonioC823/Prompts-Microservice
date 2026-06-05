import os
from google import genai

def generate_prompt(request_text, details=None):
    """Generate a prompt using Gemini AI."""

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        return "Error: GEMINI_API_KEY environment variable is not set."

    client = genai.Client(api_key=api_key)

    full_request = request_text.strip()

    if details:
        full_request += f"\n\nAdditional details:\n{details}"

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=full_request
        )

        return response.text.strip()

    except Exception as error:
        return f"Error: {error}"