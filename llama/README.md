# 💬 TinyLlama Chatbot using LangChain & Streamlit

A lightweight chatbot built using **TinyLlama** via `langchain-ollama` and Streamlit for a real-time chat interface.

## 🚀 Features

- 💡 Chat with TinyLlama through a web interface  
- 📜 Chat history maintained using Streamlit's session state  
- ⚡ Real-time streaming responses from the model  
- 🧠 Powered by LangChain and TinyLlama via Ollama  

## 📂 File Structure

```
├── chatbot_app.py           # Main Streamlit chatbot application  
├── requirements.txt         # Required dependencies  
├── README.md                # Project documentation  
```

## ▶️ How to Run

1. **Install Ollama and pull the TinyLlama model**  
   [Get Ollama](https://ollama.com) (required to run TinyLlama locally)

```bash
ollama pull tinyllama
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Launch the Streamlit app:**
```bash
streamlit run chatbot_app.py
```

## 🛠️ Tech Stack

- **Python**
- **Streamlit** – Web UI  
- **LangChain** – Model handling & chat logic  
- **Ollama** – Local LLM runtime  
- **TinyLlama** – Lightweight language model  

---

👨‍💻 **Developed by Manish Kumar Rajak**
