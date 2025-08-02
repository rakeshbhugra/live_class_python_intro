#!/usr/bin/env python3
"""
CLI script to run the chatbot
Usage: python cli.py
"""

import sys
from chatbot import Chatbot

def main():
    print("🤖 Welcome to the AI Chatbot!")
    print("Type 'exit' or 'quit' to end the conversation")
    print("-" * 40)
    
    try:
        chatbot = Chatbot(model_name="gemini/gemini-1.5-flash")
        
        while True:
            user_query = input("\nYou: ").strip()
            
            if user_query.lower() in ['exit', 'quit']:
                print("Goodbye! 👋")
                break
            
            if not user_query:
                print("Please enter a message or type 'exit' to quit.")
                continue
            
            try:
                response = chatbot.get_ai_response(user_query)
                print(f"AI: {response}")
            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")
                
    except KeyboardInterrupt:
        print("\n\nGoodbye! 👋")
        sys.exit(0)
    except Exception as e:
        print(f"Failed to initialize chatbot: {e}")
        print("Make sure you have set up your environment variables correctly.")
        sys.exit(1)

if __name__ == "__main__":
    main()