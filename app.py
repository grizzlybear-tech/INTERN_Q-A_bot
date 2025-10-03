import streamlit as st
from langchain_community.llms import HuggingFaceHub
import os

# --- Configuration ---
MODEL_ID = "mistralai/Mistral-7B-Instruct-v0.2" 

# --- Streamlit Setup ---
st.set_page_config(page_title="Mistral Q&A Bot 🤖", layout="centered")
st.title("Tiny AI Q&A Bot with Mistral 7B")
st.caption(f"Powered by {MODEL_ID} via Hugging Face API")

# Load Hugging Face API Token from Streamlit secrets or environment variables
try:
    hf_api_token = st.secrets["HUGGINGFACEHUB_API_TOKEN"]
except (AttributeError, KeyError):
    hf_api_token = os.environ.get("HUGGINGFACEHUB_API_TOKEN")

if not hf_api_token:
    st.error("Hugging Face API Token not found. Please set it in `.streamlit/secrets.toml` or as an environment variable `HUGGINGFACEHUB_API_TOKEN`.")
    st.stop()
    
# --- Initialize LangChain Component ---

@st.cache_resource
def load_llm():
    """Initializes and caches the HuggingFaceHub LLM."""
    try:
        llm = HuggingFaceHub(
            repo_id=MODEL_ID,
            huggingfacehub_api_token=hf_api_token,
            model_kwargs={"temperature": 0.1, "max_new_tokens": 512}
        )
        return llm
    except Exception as e:
        st.error(f"Error initializing LLM: {e}")
        return None

llm = load_llm()

# --- Chat History Management ---

if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({"role": "assistant", "content": "Hello! Ask me any question you have."})

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- Main Q&A Logic ---

if prompt := st.chat_input("Ask a question..."):
    # 1. Display user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 2. Get AI response
    with st.spinner("Thinking..."):
        try:
            # Mistral Prompt Formatting
            full_prompt = f"<s>[INST] {prompt} [/INST]"
            response = llm.invoke(full_prompt).strip()
            
            # Clean up the response
            if response.endswith("</s>"):
                response = response[:-4].strip()
                
            if not response or response.startswith("[INST]"):
                 response = "Sorry, I had trouble generating a clear response. Can you rephrase your question?"

            # 3. Display assistant message
            with st.chat_message("assistant"):
                st.markdown(response)

            # 4. Save assistant message to history
            st.session_state.messages.append({"role": "assistant", "content": response})
            
        except Exception as e:
            error_message = f"An error occurred: {e}"
            st.error(error_message)
            st.session_state.messages.append({"role": "assistant", "content": error_message})