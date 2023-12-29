import openai

def chat_with_bot(prompt):
    openai.api_key = 'YOUR_API_KEY'  # Replace with your OpenAI API key

    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # Choose the appropriate model
            prompt=prompt,
            max_tokens=150  # Adjust as needed
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main():
    print("Welcome to the ChatBot! Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break
        bot_response = chat_with_bot(user_input)
        print(f"Bot: {bot_response}")

if __name__ == "__main__":
    main()
