import openai

# If you stored your API key as an environment variable:
# Make sure you ran: export OPENAI_API_KEY="your_api_key_here" (Linux/Mac)
# Or: setx OPENAI_API_KEY "your_api_key_here" (Windows PowerShell)

def test_openai():
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",  # lightweight, fast model
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Say hello and tell me the current year."}
            ]
        )
        print("✅ OpenAI connection successful!")
        print("Assistant reply:\n", response["choices"][0]["message"]["content"])
    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    test_openai()
