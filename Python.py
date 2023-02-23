import openai
import json

openai.api_key = "YOUR_API_KEY"

def get_response(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return response.choices[0].text.strip()

print("Hello! I'm your chatbot. How can I help you today?")
while True:
    user_input = input("> ")
    if user_input.lower() in ["exit", "quit", "bye", "goodbye"]:
        break
    prompt = f"User: {user_input}\nBot:"
    response = get_response(prompt)
    print(response)
