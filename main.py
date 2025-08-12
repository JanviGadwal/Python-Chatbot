import re

def preprocess(text):

    text = text.lower().strip()
    text = re.sub(r'[^\w\s]', "", text)
    return text

def response(user_text):

    t = preprocess(user_text)

    if any(word in t.split() for word in ["hi", "hello", "hey", "hola"]):
        return "I am your virtual friend - a simple rule- based bot. How can I help you?"

    if "how are you" in t or "how are you doing" in t:
        return "I'm a program, so I don't have feelings — but I'm ready to help! " 
    
    if "your name" in t or "who are you" in t:
        return "I'm chatter-box — a tiny Python chatbot built with if/else rules."

    if any(word in t for word in ["thank", "thanks", "thankyou", "thank you"]):
        return "You're welcome! Anything else I can help with?"
    if any(kw in t for kw in ["help", "what can you do", "commands"]):
        return ("I can do simple conversation and a few canned responses. "
                "Try: 'hi', 'how are you', 'what is your name', 'tell me a joke', or 'exit' to quit.")
    
    if "joke" in t:
        return "C++ got it right! Your parents can’t touch your privates.. But your friends can."
    
    if "weather" in t:
        return "I can't check live weather here, but you can try 'Check weather' with an internet-enabled tool."

    if "time" in t:
        return "I can't fetch real time in this offline example, but you can ask your system clock."
    
    if any(word in t.split() for word in ["bye", "exit", "quit", "goodbye", "see you"]):
        return "Goodbye! Have a great day."
    
    return "Sorry, I don't understand that yet. Try 'help' for suggestions."

def main():
    print("Welcome to chatter-box -- a simple rule-based chatbot.")
    print("Type 'exit' or 'quit' to end the chat.\n")

    while True:
        user_input = input("You: ").strip()
        if not user_input:
            print("Bot : Please say something or type 'help'.")
            continue 

        reply = response(user_input)
        print("Bot: ", reply)

        if any(w in preprocess(user_input).split() for w in ["exit", "quit", "bye", "goodbye"]):
            break

if __name__== "__main__":
    main()