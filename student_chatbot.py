print("Student AI Chatbot")
print("Type 'exit' to stop")

while True:
    question = input("You: ").lower()

    if question == "hello":
        print("Bot: Hello! How can I help you?")
    elif question == "study tips":
        print("Bot: Make a timetable and revise daily.")
    elif question == "exam":
        print("Bot: Practice previous papers and stay calm.")
    elif question == "exit":
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: Sorry, I don't understand.")
