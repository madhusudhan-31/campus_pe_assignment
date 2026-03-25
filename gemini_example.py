# gemini_example_updated.py
# Uses NEW Google GenAI SDK (google-genai)

import os
from dotenv import load_dotenv
from google import genai

# Load API keys from .env file
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("GOOGLE_API_KEY not found. Please set it in your .env file.")

# Create client
client = genai.Client(api_key=api_key)


def query_gemini(prompt: str) -> str:
    """
    Send a prompt to Google Gemini and return the response.
    """
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash", 
            contents=prompt,
            config={
                "temperature": 0.7,
                "top_p": 0.9,
                "max_output_tokens": 500,
            }
        )

        return response.text if response.text else "No response generated."

    except Exception as e:
        error_msg = str(e)

        if "API_KEY_INVALID" in error_msg:
            return "Invalid API key. Check your GOOGLE_API_KEY."

        if "quota" in error_msg.lower():
            return "API quota exceeded. Try again later."

        if "not found" in error_msg.lower():
            return "Model not available. Try 'gemini-1.5-pro'."

        return f"Error talking to Gemini: {error_msg}"


# ── Main ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 50)
    print("  Google Gemini — Generative AI (Updated SDK)")
    print("=" * 50)

    user_prompt = input("\nEnter your prompt: ").strip()

    if not user_prompt:
        print("No prompt entered. Exiting.")
    else:
        print("\nQuerying Gemini...\n")
        response = query_gemini(user_prompt)
        print("Response:")
        print("-" * 40)
        print(response)
        print("-" * 40)