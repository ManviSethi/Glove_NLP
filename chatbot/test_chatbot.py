"""
Unit tests for the chatbot engine
Run with: python3 test_chatbot.py
"""

import unittest
import os
import sys
import json

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from chatbot_engine import ChatBot


class TestChatBot(unittest.TestCase):
    """Test cases for ChatBot class."""
    
    @classmethod
    def setUpClass(cls):
        """Set up test fixtures."""
        cls.chatbot = ChatBot('intents.json')
    
    def test_initialization(self):
        """Test chatbot initialization."""
        self.assertIsNotNone(self.chatbot)
        self.assertIsNotNone(self.chatbot.intents)
        self.assertIn('intents', self.chatbot.intents)
        self.assertIsInstance(self.chatbot.intents['intents'], list)
    
    def test_tokenization(self):
        """Test text tokenization."""
        tokens = self.chatbot._tokenize("Hello, World!")
        self.assertEqual(tokens, ['hello', 'world'])
        
        tokens = self.chatbot._tokenize("What's your name?")
        self.assertEqual(tokens, ['whats', 'your', 'name'])
    
    def test_similarity_computation(self):
        """Test similarity computation between token sets."""
        tokens1 = ['hello', 'world']
        tokens2 = ['hello', 'world']
        similarity = self.chatbot._compute_similarity(tokens1, tokens2)
        self.assertEqual(similarity, 1.0)
        
        tokens1 = ['hello', 'world']
        tokens2 = ['goodbye', 'universe']
        similarity = self.chatbot._compute_similarity(tokens1, tokens2)
        self.assertEqual(similarity, 0.0)
        
        tokens1 = ['hello', 'world']
        tokens2 = ['hello', 'universe']
        similarity = self.chatbot._compute_similarity(tokens1, tokens2)
        self.assertGreater(similarity, 0.0)
        self.assertLess(similarity, 1.0)
    
    def test_greeting_intent(self):
        """Test greeting intent recognition."""
        response = self.chatbot.get_response("Hello")
        self.assertIsInstance(response, str)
        self.assertTrue(len(response) > 0)
        
        response = self.chatbot.get_response("Hi")
        self.assertIsInstance(response, str)
        self.assertTrue(len(response) > 0)
    
    def test_name_intent(self):
        """Test name intent recognition."""
        response = self.chatbot.get_response("What is your name")
        self.assertIsInstance(response, str)
        self.assertTrue(len(response) > 0)
    
    def test_joke_intent(self):
        """Test joke intent recognition."""
        response = self.chatbot.get_response("Tell me a joke")
        self.assertIsInstance(response, str)
        self.assertTrue(len(response) > 0)
    
    def test_thanks_intent(self):
        """Test thanks intent recognition."""
        response = self.chatbot.get_response("Thank you")
        self.assertIsInstance(response, str)
        self.assertTrue(len(response) > 0)
    
    def test_unknown_input(self):
        """Test handling of unknown input."""
        response = self.chatbot.get_response("xyzabcdefghijk123456")
        self.assertIsInstance(response, str)
        self.assertTrue(len(response) > 0)
    
    def test_empty_input(self):
        """Test handling of empty input."""
        response = self.chatbot.get_response("")
        self.assertIsInstance(response, str)
        self.assertTrue(len(response) > 0)
    
    def test_fallback_response(self):
        """Test fallback response generation."""
        response = self.chatbot._get_fallback_response()
        self.assertIsInstance(response, str)
        self.assertTrue(len(response) > 0)
    
    def test_vocabulary_building(self):
        """Test vocabulary building."""
        self.assertIsInstance(self.chatbot.vocabulary, set)
        self.assertGreater(len(self.chatbot.vocabulary), 0)
    
    def test_intent_patterns(self):
        """Test intent patterns structure."""
        self.assertIsInstance(self.chatbot.intent_patterns, dict)
        self.assertGreater(len(self.chatbot.intent_patterns), 0)


def run_tests():
    """Run all tests."""
    print("=" * 70)
    print("Running ChatBot Unit Tests")
    print("=" * 70)
    
    # Create test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(TestChatBot)
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "=" * 70)
    print(f"Tests run: {result.testsRun}")
    print(f"Successes: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print("=" * 70)
    
    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
