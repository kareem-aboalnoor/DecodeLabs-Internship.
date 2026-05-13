"""
Rule-Based AI Chatbot using if-else statements
Handles greetings, questions, and commands in a continuous loop
"""

def chatbot_response(user_input):
    """Generate chatbot response based on if-else rules"""
    user_input = user_input.lower().strip()
    
    # Greeting rules
    if user_input == "hello" or user_input == "hi" or user_input == "hey":
        return "Hello! How can I help you today?"
    
    elif user_input == "good morning":
        return "Good morning! Have a great day ahead!"
    
    elif user_input == "good evening":
        return "Good evening! Hope you had a wonderful day!"
    
    elif user_input == "good night":
        return "Good night! Sleep well!"
    
    # Question: How are you?
    elif user_input == "how are you?" or user_input == "how are you":
        return "I'm doing great, thank you for asking! How about you?"
    
    # Question: What is your name?
    elif user_input == "what is your name?" or user_input == "who are you?":
        return "I'm a Rule-Based Chatbot created to assist you!"
    
    # Question: What can you do?
    elif user_input == "what can you do?" or user_input == "what are your features?":
        return "I can greet you, answer questions, and have conversations using if-else rules!"
    
    # Question: What is your purpose?
    elif user_input == "what is your purpose?" or user_input == "why do you exist?":
        return "My purpose is to provide helpful responses based on predefined rules!"
    
    # Help command
    elif user_input == "help" or user_input == "?":
        return "I can respond to greetings and questions. Try saying 'hello', 'how are you?', or 'what is your name?'"
    
    # Gratitude
    elif user_input == "thank you" or user_input == "thanks" or user_input == "thank you so much":
        return "You're welcome! Feel free to ask me anything!"
    
    # Apology
    elif user_input == "sorry" or user_input == "i'm sorry":
        return "No problem at all! Don't worry about it."
    
    # Farewell commands
    elif user_input == "goodbye" or user_input == "bye" or user_input == "see you":
        return "Goodbye! It was nice talking to you. See you later!"
    
    elif user_input == "quit" or user_input == "exit":
        return "exit"
    
    # Default response for unknown input
    else:
        return "I didn't understand that. Type 'help' to see what I can do!"


def main():
    """Main function to run the chatbot"""
    print("=" * 50)
    print("Welcome to Rule-Based Chatbot!")
    print("Type 'quit' or 'exit' to leave")
    print("=" * 50)
    print()
    
    while True:
        user_input = input("You: ").strip()
        
        if not user_input:
            continue
        
        response = chatbot_response(user_input)
        
        if response == "exit":
            print("Bot: Goodbye! Thanks for chatting with me!")
            break
        
        print(f"Bot: {response}")
        print()


if __name__ == "__main__":
    main()
