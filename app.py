import getpass

import os

from langchain_core import messages

from langchain_groq import ChatGroq # We can import any Groq or It chatmodel but prefered the chatmodel in langchain 3 version.

from langchain_core.messages import  SystemMessage, HumanMessage, AIMessage

from langchain_groq import ChatGroq # We can import any Groq or It chatmodel but prefered the chatmodel in langchain 3 version.

from langchain_core.messages import  SystemMessage, HumanMessage, AIMessage

# To store the Api key tempararely:
os.environ["GROQ_API_KEY"] = getpass.getpass("Enter your Groq API key: ")

# we are going to used model
model=ChatGroq(model="llama-3.3-70b-versatile")
# We are going to keep the history of our chat
chat_history = [
     SystemMessage(content="You are a helpful assistant.")
]

# Loop to continuously check the responses
while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))

    if user_input.lower() == "exit":
        break

    # Invoke the model by passing the chat history
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))

    print("AI:", result.content)
    print(chat_history)
