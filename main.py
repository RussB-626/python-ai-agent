import os
import sys

from dotenv import load_dotenv

from google import genai
from google.genai import types

def main():
  try:

    # Handle if no argument is passed into the prompt
    if len(sys.argv) == 1:
       print("Usage: uv run main.py <prompt>")
       sys.exit(1)

    user_prompt = sys.argv[1]
    secondary_args = sys.argv[2:]
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    messages = [
      types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    # Provide the agent with the user's prompt
    response = client.models.generate_content(
      model='gemini-2.0-flash-001',
      contents=messages
    )

    # Print out the agent's response
    if "--verbose" in secondary_args:
      print(f"User prompt: {user_prompt}")
      print(f"Prompt tokens: {str(response.usage_metadata.prompt_token_count)}")
      print(f"Response tokens: {str(response.usage_metadata.candidates_token_count)}")

    print("Response:")
    print(response.text)

  # Print out any errors to the console
  except Exception as e:
     print(f"Error Encountered: {e}")

if __name__ == "__main__":
    main()
