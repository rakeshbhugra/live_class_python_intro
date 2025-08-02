from chatbot import Chatbot

chatbot = Chatbot(model_name="gemini/gemini-1.5-flash")

while True:
    user_query = input("You: ")

    if user_query.lower() == 'exit':
        break

    try:
        response = chatbot.get_ai_response(user_query)
        print("AI:", response)
    except ValueError as e:
        print(f"Error: {e}")