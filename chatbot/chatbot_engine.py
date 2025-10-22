"""
Chatbot Engine - Core NLP-based chatbot implementation
Implements intent recognition and response generation
"""

import json
import random
import re
import string
from typing import List, Dict, Tuple, Optional


class ChatBot:
    """
    A simple NLP-based chatbot that uses pattern matching and TF-IDF
    to understand user intents and generate appropriate responses.
    """
    
    def __init__(self, intents_file: str = 'intents.json'):
        """
        Initialize the chatbot with intents data.
        
        Args:
            intents_file: Path to the JSON file containing intents
        """
        self.intents_file = intents_file
        self.intents = self._load_intents()
        self.vocabulary = set()
        self.intent_patterns = {}
        self._build_vocabulary()
        
    def _load_intents(self) -> Dict:
        """Load intents from JSON file."""
        try:
            with open(self.intents_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Error: Could not find {self.intents_file}")
            return {"intents": []}
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON in {self.intents_file}")
            return {"intents": []}
    
    def _build_vocabulary(self):
        """Build vocabulary from all patterns in intents."""
        for intent in self.intents.get('intents', []):
            tag = intent['tag']
            self.intent_patterns[tag] = []
            
            for pattern in intent.get('patterns', []):
                tokens = self._tokenize(pattern)
                self.vocabulary.update(tokens)
                self.intent_patterns[tag].append(tokens)
    
    def _tokenize(self, text: str) -> List[str]:
        """
        Tokenize and normalize text.
        
        Args:
            text: Input text to tokenize
            
        Returns:
            List of tokens
        """
        # Convert to lowercase
        text = text.lower()
        
        # Remove punctuation
        text = text.translate(str.maketrans('', '', string.punctuation))
        
        # Split into words
        tokens = text.split()
        
        return tokens
    
    def _compute_similarity(self, tokens1: List[str], tokens2: List[str]) -> float:
        """
        Compute similarity between two token lists using Jaccard similarity.
        
        Args:
            tokens1: First list of tokens
            tokens2: Second list of tokens
            
        Returns:
            Similarity score between 0 and 1
        """
        set1 = set(tokens1)
        set2 = set(tokens2)
        
        if not set1 and not set2:
            return 0.0
        
        intersection = set1.intersection(set2)
        union = set1.union(set2)
        
        if not union:
            return 0.0
            
        return len(intersection) / len(union)
    
    def _find_best_intent(self, user_input: str) -> Tuple[Optional[str], float]:
        """
        Find the best matching intent for user input.
        
        Args:
            user_input: User's message
            
        Returns:
            Tuple of (intent_tag, confidence_score)
        """
        user_tokens = self._tokenize(user_input)
        
        best_intent = None
        best_score = 0.0
        
        for intent in self.intents.get('intents', []):
            tag = intent['tag']
            
            for pattern_tokens in self.intent_patterns.get(tag, []):
                similarity = self._compute_similarity(user_tokens, pattern_tokens)
                
                if similarity > best_score:
                    best_score = similarity
                    best_intent = tag
        
        return best_intent, best_score
    
    def get_response(self, user_input: str, threshold: float = 0.3) -> str:
        """
        Generate a response to user input.
        
        Args:
            user_input: User's message
            threshold: Minimum confidence threshold for intent matching
            
        Returns:
            Chatbot's response
        """
        if not user_input.strip():
            return "I didn't catch that. Could you please say something?"
        
        intent_tag, confidence = self._find_best_intent(user_input)
        
        if confidence < threshold:
            return self._get_fallback_response()
        
        # Find the intent and get a random response
        for intent in self.intents.get('intents', []):
            if intent['tag'] == intent_tag:
                responses = intent.get('responses', [])
                if responses:
                    return random.choice(responses)
        
        return self._get_fallback_response()
    
    def _get_fallback_response(self) -> str:
        """Get a fallback response when no intent matches."""
        fallback_responses = [
            "I'm not sure I understand. Could you rephrase that?",
            "I didn't quite get that. Can you ask in a different way?",
            "Sorry, I'm not sure how to respond to that.",
            "I'm still learning! Could you try asking something else?",
            "That's interesting, but I'm not sure how to help with that yet."
        ]
        return random.choice(fallback_responses)
    
    def chat(self):
        """Start an interactive chat session."""
        print("=" * 60)
        print("ChatBot: Hello! I'm your friendly chatbot.")
        print("ChatBot: Type 'quit', 'exit', or 'bye' to end the conversation.")
        print("=" * 60)
        
        while True:
            try:
                user_input = input("\nYou: ").strip()
                
                if not user_input:
                    continue
                
                # Check for exit commands
                if user_input.lower() in ['quit', 'exit', 'bye', 'goodbye']:
                    print("\nChatBot: Goodbye! Have a great day!")
                    break
                
                response = self.get_response(user_input)
                print(f"\nChatBot: {response}")
                
            except KeyboardInterrupt:
                print("\n\nChatBot: Goodbye! Have a great day!")
                break
            except Exception as e:
                print(f"\nChatBot: Sorry, something went wrong: {e}")
                continue


if __name__ == "__main__":
    # Create and run the chatbot
    chatbot = ChatBot('intents.json')
    chatbot.chat()
