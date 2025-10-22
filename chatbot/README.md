# Chatbot - NLP-Based Conversational AI

A simple yet powerful chatbot built from scratch using Natural Language Processing techniques. This chatbot uses intent recognition and pattern matching to understand user queries and provide relevant responses.

## Features

- **Intent Recognition**: Understands user intent using pattern matching and similarity algorithms
- **Natural Language Processing**: Tokenizes and processes user input
- **Extensible Design**: Easy to add new intents and responses
- **Interactive Chat**: Command-line interface for real-time conversations
- **Fallback Handling**: Graceful handling of unknown queries
- **No External ML Libraries Required**: Built using pure Python with basic NLP techniques

## Project Structure

```
chatbot/
├── main.py              # Main entry point for the chatbot
├── chatbot_engine.py    # Core chatbot logic and NLP processing
├── intents.json         # Training data with intents, patterns, and responses
└── README.md            # This file
```

## Installation

1. **Clone the repository** (if you haven't already):
   ```bash
   git clone https://github.com/ManviSethi/Glove_NLP.git
   cd Glove_NLP/chatbot
   ```

2. **No additional dependencies required!** The chatbot uses only Python standard library and NumPy (which is commonly available).

3. **Optional**: If NumPy is not installed:
   ```bash
   pip install numpy
   ```

## Usage

### Running the Chatbot

Simply run the main script:

```bash
python3 main.py
```

Or make it executable and run directly:

```bash
chmod +x main.py
./main.py
```

### Interacting with the Chatbot

Once started, you can type messages and the chatbot will respond:

```
============================================================
ChatBot: Hello! I'm your friendly chatbot.
ChatBot: Type 'quit', 'exit', or 'bye' to end the conversation.
============================================================

You: Hello
ChatBot: Hi there! What can I do for you?

You: What's your name?
ChatBot: You can call me ChatBot!

You: Tell me a joke
ChatBot: Why don't programmers like nature? It has too many bugs!

You: Thanks
ChatBot: You're welcome!

You: bye
ChatBot: Goodbye! Have a great day!
```

### Exit Commands

To end the conversation, type any of:
- `quit`
- `exit`
- `bye`
- `goodbye`
- Or press `Ctrl+C`

## How It Works

### Intent Recognition

The chatbot uses a **Jaccard similarity** algorithm to match user input with predefined patterns:

1. **Tokenization**: User input is converted to lowercase, punctuation is removed, and text is split into tokens
2. **Pattern Matching**: Each token set is compared with patterns in the intents file
3. **Similarity Scoring**: Jaccard similarity measures the overlap between user input and patterns
4. **Intent Selection**: The intent with the highest similarity score (above threshold) is selected
5. **Response Generation**: A random response is selected from the matched intent's response list

### Intents File Structure

The `intents.json` file contains all the training data:

```json
{
  "intents": [
    {
      "tag": "greeting",
      "patterns": [
        "Hi",
        "Hello",
        "Hey"
      ],
      "responses": [
        "Hello! How can I help you today?",
        "Hi there! What can I do for you?"
      ]
    }
  ]
}
```

## Customization

### Adding New Intents

To add new conversation topics, edit `intents.json`:

1. Add a new intent object with:
   - `tag`: Unique identifier for the intent
   - `patterns`: List of example user inputs
   - `responses`: List of possible bot responses

Example:
```json
{
  "tag": "hobbies",
  "patterns": [
    "What are your hobbies",
    "What do you like to do",
    "What are your interests"
  ],
  "responses": [
    "I enjoy chatting with people like you!",
    "I love learning new things from conversations!"
  ]
}
```

2. Restart the chatbot to load the new intents

### Adjusting Confidence Threshold

In `chatbot_engine.py`, you can modify the threshold parameter in the `get_response()` method to make the chatbot more or less strict in matching intents:

```python
response = chatbot.get_response(user_input, threshold=0.3)  # Default is 0.3
```

- Lower threshold (e.g., 0.1): More lenient, may match more queries but less accurately
- Higher threshold (e.g., 0.5): More strict, better accuracy but may miss some valid queries

## Built-in Intents

The chatbot comes with the following pre-configured intents:

1. **Greeting**: Handle hello, hi, and other greetings
2. **Goodbye**: Handle farewell messages
3. **Thanks**: Acknowledge gratitude
4. **About**: Explain chatbot's purpose
5. **Name**: Share the chatbot's name
6. **Help**: Offer assistance
7. **Age**: Respond to age-related questions
8. **Weather**: Handle weather queries (with disclaimers)
9. **Joke**: Tell jokes
10. **Time**: Handle time-related queries (with disclaimers)
11. **No Answer**: Handle uncertain user responses

## Technical Details

### Algorithms Used

- **Tokenization**: Basic string processing and normalization
- **Jaccard Similarity**: Set-based similarity measurement
  ```
  Similarity = |A ∩ B| / |A ∪ B|
  ```
  where A and B are token sets

### Dependencies

- Python 3.6+
- NumPy (optional, for potential future enhancements)

## Future Enhancements

Potential improvements for the chatbot:

- [ ] Add spell checking and correction
- [ ] Implement context awareness for multi-turn conversations
- [ ] Add sentiment analysis
- [ ] Integrate with machine learning models (e.g., word embeddings)
- [ ] Support for multiple languages
- [ ] Web interface using Flask or FastAPI
- [ ] Persistent conversation history
- [ ] User profile management

## Contributing

To contribute to this chatbot:

1. Fork the repository
2. Create a new branch for your feature
3. Add your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is part of the Glove_NLP repository.

## Support

If you encounter any issues or have questions:
- Check the existing intents in `intents.json`
- Ensure all files are in the correct directory
- Verify Python version compatibility (3.6+)

## Acknowledgments

Built from scratch as a learning project to demonstrate NLP concepts and chatbot development.
