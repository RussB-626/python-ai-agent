import os
import sys
from google import genai
from dotenv import load_dotenv

def main():
  try:
    if len(sys.argv) == 1:
       print("Usage: uv run main.py <prompt>")
       sys.exit(1)

    user_prompt = sys.argv[1]
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
      model='gemini-2.0-flash-001',
      contents=user_prompt
    )
    print("Prompt tokens: " + str(response.usage_metadata.prompt_token_count))
    print("Response tokens: " + str(response.usage_metadata.candidates_token_count))
    print("Response:")
    print(response.text)

  except Exception as e:
     print(f"Error Encountered: {e}")


if __name__ == "__main__":
    main()
