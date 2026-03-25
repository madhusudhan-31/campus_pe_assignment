import os
from dotenv import load_dotenv
import cohere


load_dotenv()
api_key = os.getenv("COHERE_API_KEY")

if not api_key:
    raise ValueError("COHERE_API_KEY not found in .env file.")


co = cohere.ClientV2(api_key)


def query_cohere(prompt: str) -> str:
    try:
        response = co.chat(
            model="command-a-03-2025",  
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500
        )

        return response.message.content[0].text.strip()

    except Exception as e:
        return f"Error: {str(e)}"



if __name__ == "__main__":
    print("=" * 50)
    print("  Cohere — Chat")
    print("=" * 50)

    user_prompt = input("\nEnter your prompt: ").strip()

    if not user_prompt:
        print("No prompt entered.")
    else:
        print("\nQuerying Cohere...\n")
        response = query_cohere(user_prompt)
        print("Response:")
        print("-" * 40)
        print(response)
        print("-" * 40)