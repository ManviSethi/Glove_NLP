#!/usr/bin/env python3
"""
Main Chatbot Application
Run this script to start chatting with the bot
"""

import os
import sys

# Add the chatbot directory to the path
chatbot_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, chatbot_dir)

from chatbot_engine import ChatBot


def main():
    """Main function to run the chatbot."""
    # Get the intents file path
    intents_path = os.path.join(chatbot_dir, 'intents.json')
    
    # Check if intents file exists
    if not os.path.exists(intents_path):
        print(f"Error: intents.json not found at {intents_path}")
        sys.exit(1)
    
    # Create and run the chatbot
    chatbot = ChatBot(intents_path)
    chatbot.chat()


if __name__ == "__main__":
    main()
