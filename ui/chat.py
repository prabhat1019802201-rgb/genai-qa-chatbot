import streamlit as st
from llm.llm_factory import get_llm
from chains.qa_chain import get_chat_chain

def render_chat_ui():
    st.markdown("## 💬 Chat")

    # ----------------------------------
    # Initialize Chat History
    # ----------------------------------
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # ----------------------------------
    # Display Chat History
    # ----------------------------------
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # ----------------------------------
    # User Input
    # ----------------------------------
    user_input = st.chat_input("Ask your question...")

    if user_input:
        # Add user message
        st.session_state.messages.append(
            {"role": "user", "content": user_input}
        )

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    llm = get_llm(
                        provider=st.session_state.provider,
                        api_key=st.session_state.api_key,
                        model=st.session_state.model,
                        temperature=st.session_state.temperature,
                        max_tokens=st.session_state.max_tokens,
                    )

                    chain = get_chat_chain(llm)

                    response = chain.invoke(
                        {
                            "question": user_input,
                            "history": [
                                (m["role"], m["content"])
                                for m in st.session_state.messages[:-1]
                            ],
                        }
                    )

                except Exception as e:
                    response = f"❌ Error: {str(e)}"

            st.markdown(response)

        # Add assistant message
        st.session_state.messages.append(
            {"role": "assistant", "content": response}
        )

        st.rerun()
