import os
from dotenv import load_dotenv

load_dotenv()

from google import genai
gemini_client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def gemini_ai(prompt):
    response = gemini_client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    return response.text


from groq import Groq
groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def groq_ai(prompt):
    response = groq_client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.1-8b-instant",
    )
    return response.choices[0].message.content



import cohere
cohere_client = cohere.ClientV2(os.getenv("COHERE_API_KEY"))

def cohere_ai(prompt):
    response = cohere_client.chat(
        model="command-a-03-2025",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.message.content[0].text


from huggingface_hub import InferenceClient
hf_client = InferenceClient(token=os.getenv("HUGGINGFACE_API_KEY"))

def hf_ai(prompt):
    response = hf_client.chat_completion(
        model="meta-llama/Meta-Llama-3-8B-Instruct",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content


def smart_ai(prompt, choice):
    try:
        if choice == "1":
            return gemini_ai(prompt)

        elif choice == "2":
            return groq_ai(prompt)

        elif choice == "3":
            return cohere_ai(prompt)

        elif choice == "4":
            return hf_ai(prompt)

        elif choice == "5":
            if len(prompt) < 50:
                return groq_ai(prompt)
            else:
                return gemini_ai(prompt)

        else:
            return "Invalid choice."

    except Exception as e:
        print("Error:", e)
        return "Failed to get response."


if __name__ == "__main__":
    print("=" * 50)
    print("  Multi-AI System (Choose Your Model)")
    print("=" * 50)

    print("""
Select AI Model:
1. Gemini 
2. Groq 
3. Cohere 
4. HuggingFace 
5. Auto Mode 
""")

    choice = input("Enter choice (1-5): ").strip()
    prompt = input("\nEnter your prompt: ").strip()

    print("\nThinking...\n")
    result = smart_ai(prompt, choice)

    print("Response:")
    print("-" * 40)
    print(result)
    print("-" * 40)