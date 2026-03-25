

import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# Load API key
load_dotenv()
api_key = os.getenv("HUGGINGFACE_API_KEY")

if not api_key:
    raise ValueError("HUGGINGFACE_API_KEY not found. Check your .env file.")

# ✅ Create client
client = InferenceClient(token=api_key)

def query_huggingface(prompt: str) -> str:
    try:
        response = client.chat_completion(
            model="meta-llama/Meta-Llama-3-8B-Instruct", 
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=300,
            temperature=0.7,
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"Error: {str(e)}"


# ── Main ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 50)
    print("  Hugging Face — Chat")
    print("=" * 50)

    user_prompt = input("\nEnter your prompt: ").strip()

    if not user_prompt:
        print("No prompt entered. Exiting.")
    else:
        print("\nQuerying Hugging Face...\n")
        response = query_huggingface(user_prompt)
        print("Response:")
        print("-" * 40)
        print(response)
        print("-" * 40)