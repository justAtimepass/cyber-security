print("Hello! I'm a simple chatbot. Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower() 
    if user_input == "bye":
        print("Bot: Goodbye! Have a great day!")
        break 
    elif user_input == "hello":
        print("Bot: Hi there! How can I help you?")
    elif user_input == "how are you":
        print("Bot: I'm just a program, but I'm doing well! Thanks for asking.")
    elif "name" in user_input:
        print("Bot: You can call me ChatBot! What's your name?")
    elif "weather" in user_input:
        print("Bot: I don't have access to real-time weather, but I hope it's lovely where you are!")
    else:
        print("Bot: I'm sorry, I don't understand that. Can you rephrase?")
