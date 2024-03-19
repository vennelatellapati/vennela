def chatbot():
  # Greeting the user
  print("Hello! I'm a simple chatbot. How can I help you today?")
  while True:
    user_input = input("You: ")
    user_input = user_input.lower()  # Convert input to lowercase for easier matching

    # Check for greetings
    if "hi" in user_input or "hello" in user_input:
      print("Chatbot: Hi there! What would you like to know?")
    
    # Check for basic questions
    elif "your name" in user_input:
      print("Chatbot: My name is Bard, a simple chatbot!")
    elif "can you do" in user_input:
      print("Chatbot: I can answer basic questions and follow simple instructions.")
    elif "bye" in user_input or "exit" in user_input:
      print("Chatbot: Thanks for chatting! See you later.")
      break
    else:
      print("Chatbot: Sorry, I don't understand. Try asking a different question.")

if __name__ == "__main__":
  chatbot()