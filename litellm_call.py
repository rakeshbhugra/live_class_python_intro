from litellm import completion

messages = [
    {'role': 'system', 'content': 'You are a helpful assistant.'},
]

user_query = input("Enter your query: ")

messages.append({'role': 'user', 'content': user_query})

print(messages)

response = completion(
    model = "gemini/gemini-1.5-flash",
    messages = messages,
    api_key='....'
)

print("AI Response:", response['choices'][0]['message']['content'])