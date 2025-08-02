from litellm import completion

messages = [
    {'role': 'system', 'content': 'You are a helpful assistant.'},
]

# user_query = input("Enter your query: ")

# messages.append({'role': 'user', 'content': user_query})

# print(messages)

# response = completion(
#     model = "gemini/gemini-1.5-flash",
#     # model = "ollama/llama3:latest",
#     messages = messages,
#     api_key='AIzaSyCsGl_MjnKvY2Z7Lyf33CZfRaSndyiXLsQ'
# )

# print("AI Response:", response['choices'][0]['message']['content'])

while True:
    user_query = input("You: ")
    if user_query.lower() == 'exit':
        break
    
    messages.append({'role': 'user', 'content': user_query})
    
    response = completion(
        model = "gemini/gemini-1.5-flash",
        messages = messages,
        api_key='...'
    )
    
    print("AI:", response['choices'][0]['message']['content'])
    messages.append({'role': 'assistant', 'content': response['choices'][0]['message']['content']})