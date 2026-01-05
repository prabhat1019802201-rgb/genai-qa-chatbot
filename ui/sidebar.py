import streamlit as st

def render_sidebar():
    st.markdown("## 🤖 GenAI Q&A Chatbot")

    st.markdown("---")

    # -------------------------------
    # LLM Provider Selection
    # -------------------------------
    provider = st.selectbox(
        "LLM Provider",
        options=[
            "HuggingFace (Local / Free)",
            "Groq",
            "OpenAI"
        ]
    )

    # -------------------------------
    # API Key (Only when needed)
    # -------------------------------
    api_key = None
    if provider in ["Groq", "OpenAI"]:
        api_key = st.text_input(
            label=f"{provider} API Key",
            type="password",
            placeholder=f"Enter your {provider} API key"
        )

    st.markdown("---")

    # -------------------------------
    # Model Selection
    # -------------------------------
    if provider == "HuggingFace (Local / Free)":
        model = st.selectbox(
            "Model",
            options=[
                "google/flan-t5-large",
                "mistralai/Mistral-7B-Instruct-v0.2"
            ]
        )

    elif provider == "Groq":
        model = st.selectbox(
            "Model",
            options=[
                "llama-3.1-8b-instant",
                "llama-3.3-70b-versatile"
            ]
        )

    else:  # OpenAI
        model = st.selectbox(
            "Model",
            options=[
                "gpt-3.5-turbo",
                "gpt-4"
            ]
        )

    st.markdown("---")

    # -------------------------------
    # Generation Parameters
    # -------------------------------
    temperature = st.slider(
        "Temperature",
        min_value=0.0,
        max_value=1.0,
        value=0.7,
        step=0.1
    )

    max_tokens = st.slider(
        "Max Tokens",
        min_value=256,
        max_value=8192,
        value=1024,
        step=256
    )

    st.markdown("---")

    # -------------------------------
    # RAG: Document Upload
    # -------------------------------
    uploaded_files = st.file_uploader(
        "Upload PDF documents (RAG)",
        type=["pdf"],
        accept_multiple_files=True
    )

    st.markdown("---")

    # -------------------------------
    # Store in Session State
    # -------------------------------
    st.session_state.provider = provider
    st.session_state.api_key = api_key
    st.session_state.model = model
    st.session_state.temperature = temperature
    st.session_state.max_tokens = max_tokens
    st.session_state.uploaded_files = uploaded_files
