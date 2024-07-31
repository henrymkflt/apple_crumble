""" This file is for testing queries."""
import time
from openai import OpenAI

client = OpenAI(
  api_key="not_needed",
  base_url="http://1.1.1.1:8080/v1"
)

def chatbot(message):
    """Chatbot functionality."""
    # Create a list to store all the messages for context
    messages = [
      {"role": "system", "content": "You are a helpful assistant."},
    ]

    messages.append({"role": "user", "content": message})

    # Request for chat completion
    start = time.time()
    response = client.chat.completions.create(
      messages=messages,
      model=""
    )
    end = time.time()
    print (f"Took {(end - start)} seconds.")

    # Print the response and add it to the messages list
    chat_message = response.choices[0].message.content
    print(f"Bot: {chat_message}")

if __name__ == "__main__":
    print("Starting test...")

    chatbot("What are the primary colours in art?")
    time.sleep(5)
    chatbot("""Summarise this block of text:
            The wet weather caused the slowest monthly increase in grocery sales in two years as people were 
            "put off from popping to the shops", according to research firm Kantar. The cost of living also played 
            a role in the decreased spending, with nearly a quarter of households surveyed by the company saying 
            they were still struggling. However, Kantar also recorded a big jump in financially "comfortable" households 
            because of slowing price rises and predicted a boost in spending from the Euros. "The cost of living crisis 
            isn’t over - far from it," said Kantar’s head of retail and consumer insight Fraser McKevitt. “However, there 
            are positive signs that many of us no longer feel the need to restrict our spending quite so much,” he added. 
            According to Kantar's analysis, its measure of grocery price inflation was 2.1% over the four weeks to 9 June 
            and it said this was the 16th monthly period in a row the figure had fallen. It said this contributed to a rise 
            in people feeling better about their finances, with over one-third of the 10,500 people it surveyed describing 
            their financial position as comfortable, the highest figure since November 2021.
            """)
