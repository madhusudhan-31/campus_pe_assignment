from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def query_groq(prompt: str) -> str:
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "user", "content": prompt}
            ],
            model="llama-3.1-8b-instant", 
            temperature=0.7,
            max_tokens=500,
        )

        return chat_completion.choices[0].message.content

    except Exception as e:
        return f"Oops! Something went wrong: {str(e)}"


if __name__ == "__main__":
    print("=" * 50)
    print("  Groq API — LLaMA Chat (Updated)")
    print("=" * 50)

    user_prompt = input("\nEnter your prompt: ").strip()

    if not user_prompt:
        print("No prompt entered. Exiting.")
    else:
        print("\nQuerying Groq... (usually super fast!)\n")
        response = query_groq(user_prompt)
        print("Response:")
        print("-" * 40)
        print(response)
        print("-" * 40)