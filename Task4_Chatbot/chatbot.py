# CodeAlpha Internship - Task 4
# Basic Rule-Based Chatbot

def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    if user_input == "hello" or user_input == "hi":
        return "Hi! Nice to meet you!"

    elif user_input == "how are you":
        return "I'm fine, thanks!"

    elif user_input == "what is your name":
        return "I'm a simple Python chatbot."

    elif user_input == "help":
        return "You can say hello, ask how I am, ask my name, or say bye."

    elif user_input == "bye":
        return "Goodbye! Have a great day!"

    else:
        return "Sorry, I don't understand that."

print("=" * 40)
print("          BASIC CHATBOT")
print("=" * 40)
print("Type 'bye' to exit the chatbot.")

while True:
    user_input = input("\nYou: ")

    response = chatbot_response(user_input)

    print("Chatbot:", response)

    if user_input.lower().strip() == "bye":
        break

print("\nThank you for chatting!")