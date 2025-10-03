Project Development Journal
This journal documents the process, decisions, successes, and challenges encountered while building the Tiny AI Q&A Bot, fulfilling the requirement to document the entire journey.

Week 1: Setup and Initial Task Selection
Date

Activity

Outcome / Reflection

[Start Date]

Initial Setup & Task Selection

Decided on AI Q&A Bot as the core task. Installed Python, set up a virtual environment, and created the initial GitHub repository with a README.



Model Choice

Chose Mistral-7B-Instruct-v0.2 for its strong performance in instruction-following tasks and availability via the Hugging Face API.



Code Environment Setup

Installed streamlit, langchain, and huggingface_hub to simplify the connection to the model.

Week 2: Core Functionality and Obstacles
Date

Activity

Successes & Failures

[Day X]

First LLM Integration Attempt

Success: Used the HuggingFaceHub wrapper from LangChain to successfully connect to the Mistral API and get a basic text response. This confirmed the API key was valid.



Building the UI (Stretch Goal)

Chose Streamlit for its rapid development speed. Initial attempt was a simple st.text_input and st.write.



Handling Secrets (Obstacle)

Failure: Initially confused about how to manage the API key. Tried hard-coding it, which is a major security risk. Action Taken: Researched Streamlit's official documentation on secrets management, leading to the use of the secure .streamlit/secrets.toml file.



Securing the Repo

Created the crucial .gitignore file to explicitly prevent the .streamlit/ directory from being tracked and pushed to GitHub. This was a critical learning moment in security best practices.

Week 3: Refinement and Final Polish
Date

Activity

Final Steps & Learnings

[Day Y]

Implementing Chat History

Success: Incorporated st.session_state to store conversation history. This elevated the app from a single-shot query tool to a true, context-aware chatbot.



Prompt Engineering

Added the required Mistral-specific prompt template (<s>[INST] {prompt} [/INST]) to the user query before sending it to the model, ensuring optimal response quality.



File Cleanup

Removed empty/redundant files like qna_bot.py to keep the project clean and professional.



Final Documentation

Created this detailed JOURNAL.md and a professional README.md to clearly present the project and the journey.

Conclusion: This project was a highly valuable introduction to deploying LLMs in a practical application. The biggest hurdle—securely managing credentials—taught a crucial lesson in application development security.