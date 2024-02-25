from random import choice, randint
from openai import OpenAI

client = OpenAI(
    api_key="xxxxxxxxxxx")

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'Well, you\'re awfully silent...'
    elif 'hello' in lowered:
        return 'Hello there!'
    elif 'how are you' in lowered:
        return 'Good, thanks!'
    elif 'bye' in lowered:
        return 'See you!'
    elif 'roll dice' in lowered:
        return f'You rolled: {randint(1, 6)}'
    else:
        try:
            response = client.completions.create(# Update the method name as per the new API
            model="babbage-002",  # Choose a suitable ChatGPT model
            prompt=f"User: {user_input}\nChatGPT:",
            max_tokens=150,  # Adjust max response length as needed
            temperature=0.7)
            return response.choices[0].text.strip()  # Extract ChatGPT's response
        except Exception as e:
            print(f"Error using ChatGPT: {e}")
            return "I'm having trouble accessing ChatGPT at the moment. Please try again later."