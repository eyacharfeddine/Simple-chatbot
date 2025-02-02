import random
from datetime import datetime

def chatbot():
    print("Chatbot: Hi!,What's your name?")
    user_name = input("You: ").capitalize()
    print(f"Chatbot: Nice to meet you, {user_name}! How can I help you today?")
    print("Type 'help' to see what I can do or 'exit' to end the conversation.")
    
    while True:
        # Get user input
        user_input = input(f"{user_name}: ").lower()
        
        # Exit condition
        if user_input == "exit":
            print(f"Chatbot: Goodbye, {user_name}! Have a great day!")
            break
        
        # Help command
        elif user_input == "help":
            print("Chatbot: Here's what I can do:")
            print("- Greet me with 'hello' or 'hi'.")
            print("- Ask how I'm doing with 'how are you?'.")
            print("- Ask for the time or day.")
            print("- Ask me to tell a joke ('tell me a joke').")
            print("- Ask for a fun fact ('tell me a fun fact').")
            print("- Solve math problems like '2 + 2'.")
            print("- And much more!")
        
        # Greeting
        elif "hello" in user_input or "hi" in user_input:
            print(f"Chatbot: Hello, {user_name}! How can I assist you?")
        
        # Emotional Check-in
        elif "how are you" in user_input:
            print(f"Chatbot: I'm just a program, but I'm doing great! How about you, {user_name}?")
        
        # Name Query
        elif "your name" in user_input:
            print("Chatbot: I'm Chatbot, your virtual assistant.")
        
        # Current Time
        elif "time" in user_input:
            now = datetime.now().strftime("%H:%M:%S")
            print(f"Chatbot: The current time is {now}.")
        
        # Current Day
        elif "day" in user_input:
            today = datetime.now().strftime("%A")
            print(f"Chatbot: Today is {today}.")
        
        # Joke Teller
        elif "joke" in user_input:
            jokes = [
                "Why don't scientists trust atoms? Because they make up everything!",
                "What do you call fake spaghetti? An impasta!",
                "Why couldn't the bicycle stand up by itself? It was two tired!"
            ]
            print(f"Chatbot: {random.choice(jokes)}")
        
        # Fun Fact
        elif "fun fact" in user_input:
            facts = [
                "Did you know? Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still edible!",
                "Octopuses have three hearts, and two of them stop beating when they swim.",
                "Bananas are berries, but strawberries aren’t!"
            ]
            print(f"Chatbot: {random.choice(facts)}")
        
        # Math Solver
        elif any(op in user_input for op in ['+', '-', '*', '/']):
            try:
                result = eval(user_input)
                print(f"Chatbot: The result is {result}.")
            except:
                print("Chatbot: I couldn't calculate that. Please try a valid arithmetic operation.")
        
        # Fallback Response
        else:
            print("Chatbot: Sorry, I didn't understand that. Could you rephrase your question?")

# Run the chatbot
chatbot()
