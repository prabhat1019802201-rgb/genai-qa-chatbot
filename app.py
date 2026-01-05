import streamlit as st
from ui.sidebar import render_sidebar
from ui.chat import render_chat_ui
import os
from dotenv import load_dotenv
load_dotenv()

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="GenAI Q&A Chatbot",
    page_icon="🤖",
    layout="wide"
)

# --------------------------------------------------
# Custom CSS for Vertical Divider
# --------------------------------------------------
st.markdown(
    """
    <style>
        .vertical-divider {
            border-left: 2px solid #e0e0e0;
            height: 100vh;
            margin: 0 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# Session State Initialization
# --------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# --------------------------------------------------
# Layout (3 columns: left | divider | right)
# --------------------------------------------------
left_col, divider_col, right_col = st.columns([1, 0.05, 3])

with left_col:
    render_sidebar()

with divider_col:
    st.markdown('<div class="vertical-divider"></div>', unsafe_allow_html=True)

with right_col:
    render_chat_ui()
