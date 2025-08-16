# Importing Streamlit for web UI
import streamlit as st

# Importing OllamaLLM from langchain_ollama to connect with TinyLlama model
from langchain_ollama import OllamaLLM

# Initializing the TinyLlama model via Ollama
llm = OllamaLLM(model="tinyllama")

# Set Streamlit page configuration (title and layout)
st.set_page_config(page_title="💬 Chatbot", layout="wide")

# Set the main title of the web app
st.title("💬 Chat with TinyLLama")

# Check if 'messages' key exists in session_state (used to store chat history)
if "messages" not in st.session_state:
    
    # If not, initialize it with a welcome message from the assistant
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi! How can I help you today?"}
        ]
    
# Display all past messages stored in session_state
for msg in st.session_state.messages:
    
    # Display each message in a chat-style format (either user or assistant)
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
# Function to generate a streaming response from the model
def generate_response(prompt):

    # Stream the response from the model
    stream = llm.stream(prompt)


   # To collect full message
    full_response = ""
    for chunk in stream:
   
      # Append each chunk to the response
     full_response += chunk  
    
      # Yield chunk to display it in real-time
     yield chunk 
      
    # After completion, save full response to message history
    st.session_state.messages.append({"role": "assistant", "content": full_response})

# If user inputs a new prompt (detected via chat_input)
if prompt := st.chat_input("Type your message here..."):

    # Save user's message to session_state
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display user's message in chat
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Display assistant's streamed response
    with st.chat_message("assistant"):
        st.write_stream(generate_response(prompt))
        
