import random
import re
# Define patterns and corresponding responses for the shopkeeper
shopkeeper_patterns_responses = {
    r"hello|hi|hey|good (morning|afternoon|evening)": ["Hello! Welcome to our store.", "Hi there! How can I assist you?"],
    r"do you have (.*)\?": ["Yes, we have {0}.", "Let me check... Yes, we do have {0}."],
    r"how much (is|are) (.*)(\?)?": ["The price for {1} is $X.", "It costs $X for {1}."],
    r"(.*)": ["Is there anything else I can help you with?", "Let me know if you need assistance with anything else."]
}

# Define patterns and corresponding responses for the customer
customer_patterns_responses = {
    r"(hello|hi|hey|good (morning|afternoon|evening))": ["Hi! I'm looking for {0}.", "Hello! Do you have {0}?"],
    r"how much (is|are) (.*)(\?)?": ["How much does {1} cost?", "Can you tell me the price for {1}?"]
}

def respond_to_user_input(user_input, patterns_responses):
    # Iterate over patterns and responses, and return a random response for the first matching pattern
    for pattern, responses in patterns_responses.items():
        match = re.match(pattern, user_input.lower())
        if match:
            response = random.choice(responses)
            if '{0}' in response:
                response = response.format(*match.groups())
            return response

def shopkeeper_conversation():
    print("Shopkeeper: Welcome to our store! How can I help you today?")
    while True:
        user_input = input("Customer: ")
        if user_input.lower() == 'bye':
            print("Shopkeeper: Goodbye! Have a nice day!")
            break
        else:
            print("Shopkeeper:", respond_to_user_input(user_input, shopkeeper_patterns_responses))

def customer_conversation():
    print("Customer: Hello! I'm looking for something specific.")
    while True:
        user_input = input("Shopkeeper: ")
        if user_input.lower() == 'bye':
            print("Customer: Thank you! Goodbye!")
            break
        else:
            print("Customer:", respond_to_user_input(user_input, customer_patterns_responses))

def main():
    print("Welcome to the shopkeeper-customer chatbot simulation!")
    print("Let's start with the shopkeeper:")
    shopkeeper_conversation()
    print("\nNow, let's switch roles. You'll be the customer:")
    customer_conversation()

if __name__ == "__main__":
    main()
