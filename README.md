🤖 Tiny AI Q&A Bot: Mistral-Powered Streamlit App
Project Overview
This project successfully implements the AI Q&A Bot task from the intern assignment, extending it to meet the Stretch Goal of providing a functional, modern user interface.

The application uses the state-of-the-art Mistral-7B-Instruct model via the Hugging Face API, wrapped in a user-friendly Streamlit web interface. It serves as a simple, powerful demonstration of connecting a front-end application to a large language model.

🚀 Live Demo (Future Deployment)
[Link to your deployed app will go here once you deploy it on platforms like Streamlit Community Cloud or Hugging Face Spaces!]

Key Features
Real-time Q&A: Answers user queries using the powerful Mistral 7B model.

Modern UI: Built with Streamlit for a simple, responsive, and intuitive chat interface.

Conversation History: Maintains context within a single session using Streamlit's session_state.

Secure Configuration: Uses .streamlit/secrets.toml and .gitignore to securely manage the API key, ensuring private credentials are never exposed on GitHub.

⚙️ Technology Stack
Component

Technology

Purpose

Language Model (LLM)

Mistral-7B-Instruct-v0.2

The large language model providing the intelligence.

API Integration

HuggingFaceHub

Handles the communication with the Mistral model API.

Application Framework

Streamlit

Used to create the simple, interactive web user interface (Stretch Goal).

LLM Orchestration

LangChain

Provides a simple, standardized way to interact with the LLM.

Core Language

Python

The primary language for development.

🛠️ Local Setup and Run Instructions
Prerequisites
Python 3.8+ installed.

A Hugging Face API Token (read-only access).

Steps
Clone the Repository:

git clone [YOUR-REPO-URL]
cd INTERN_Q&A_bot

Install Dependencies:

pip install streamlit langchain huggingface_hub

Configure Secrets:
Create a folder named .streamlit and inside it, create a file named secrets.toml. Paste your API token in this file:

HUGGINGFACEHUB_API_TOKEN = "PASTE_YOUR_TOKEN_HERE"

Run the App:

streamlit run app.py






