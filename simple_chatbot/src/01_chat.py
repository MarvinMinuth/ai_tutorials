from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def main():
    # Create client to connect to OpenAI API
    # The API Key is automatically loaded from the environment variables, but could also be provided here, e.g.:
    # client = OpenAI(api-key="your-api-key")
    client = OpenAI()

    # We use a while loop to create an endless chat
    while True:
        # Get the user input from the command line
        query = input("User: ")

        # Add an ending condition:
        # If the user types 'quit', 'q' or 'exit' the chat stops
        if query.lower() in ["quit", "q", "exit"]:
            break

        # Use the OpenAI client to create a response using the user query as input
        response = client.responses.create(model="chatgpt-4o-latest", input=query)
        print(f"Assistant: {response.output_text}")
        print("-----------------------")


if __name__ == "__main__":
    main()
