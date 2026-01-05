import streamlit as st

def render_sidebar():
    st.markdown("## 🤖 GenAI Chatbot")

    st.markdown("---")

    # -------------------------------
    # API Key Input
    # -------------------------------
    api_key = st.text_input(
        label="LLM API Key",
        type="password",
        placeholder="Enter your API key here"
    )

    st.markdown("---")

    # -------------------------------
    # LLM Provider Selection
    # -------------------------------
    provider = st.selectbox(
        "LLM Provider",
        options=["Free LLM (Groq/HF)", "OpenAI"]
    )

    # -------------------------------
    # Model Selection
    # -------------------------------
    if provider == "OpenAI":
       model = st.selectbox(
          "Model",
          options=["gpt-3.5-turbo", "gpt-4"]
       )
    else:
       model = st.selectbox(
        "Model",
        options=[
            "llama-3.1-8b-instant",
            "llama-3.3-70b-versatile"
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
        min_value=128,
        max_value=4096,
        value=1024,
        step=128
    )

    # -------------------------------
    # Store in Session State
    # -------------------------------
    st.session_state.api_key = api_key
    st.session_state.provider = provider
    st.session_state.model = model
    st.session_state.temperature = temperature
    st.session_state.max_tokens = max_tokens
