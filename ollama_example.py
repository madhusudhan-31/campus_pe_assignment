# Simple local AI chat using a tiny model (fast + low RAM)

import requests

# Ollama runs locally
OLLAMA_URL = "http://localhost:11434"


MODEL = "tinyllama"   


def chat(prompt):
    """Send prompt to local Ollama model and get response"""
    
    url = f"{OLLAMA_URL}/api/generate"
    
    data = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False,  
        "options": {
            "temperature": 0.7,
            "num_predict": 200  
        }
    }

    try:
        res = requests.post(url, json=data, timeout=60)
        res.raise_for_status()
        return res.json().get("response", "No response")

    except Exception as e:
        return f"Error: {e}"


def show_models():
    """Show all pulled models"""
    try:
        res = requests.get(f"{OLLAMA_URL}/api/tags")
        models = res.json().get("models", [])
        return [m["name"] for m in models]
    except:
        return []


# ── MAIN ─────────────────────────────
if __name__ == "__main__":
    print("\n🧠 Local AI Chat (Lightweight Mode)")
    
    models = show_models()
    print(f"\nAvailable models: {models if models else 'None'}")
    print(f"Using model: {MODEL}\n")

    while True:
        user = input("You: ")

        if user.lower() in ["exit", "quit"]:
            print("Exiting...")
            break

        reply = chat(user)
        print(f"\nAI: {reply}\n")