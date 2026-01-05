import streamlit as st
from llm.llm_factory import get_llm
from chains.qa_chain import get_rag_chain
from rag.ingest import ingest_pdfs
from rag.retriever import get_relevant_docs
import tempfile

def render_chat_ui():
    st.markdown("## 💬 Chat")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "vectorstore" not in st.session_state:
        st.session_state.vectorstore = None

    # Display history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Handle document upload
    if st.session_state.uploaded_files and st.session_state.vectorstore is None:
        with st.spinner("Indexing documents..."):
            pdf_paths = []
            for file in st.session_state.uploaded_files:
                temp = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
                temp.write(file.read())
                pdf_paths.append(temp.name)

            st.session_state.vectorstore = ingest_pdfs(
              pdf_paths,
              provider=st.session_state.provider,
              api_key=st.session_state.api_key,
            )

        st.success("Documents indexed successfully!")

    user_input = st.chat_input("Ask your question...")

    if user_input:
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

                    chain = get_rag_chain(llm)

                    context_docs = []
                    if st.session_state.vectorstore:
                        context_docs = get_relevant_docs(
                            st.session_state.vectorstore,
                            user_input
                        )

                    context = "\n\n".join(
                        doc.page_content for doc in context_docs
                    )

                    response = chain.invoke(
                        {
                            "question": user_input,
                            "context": context,
                            "history": [
                                (m["role"], m["content"])
                                for m in st.session_state.messages[:-1]
                            ],
                        }
                    )

                except Exception as e:
                    response = f"❌ Error: {str(e)}"

            st.markdown(response)

        st.session_state.messages.append(
            {"role": "assistant", "content": response}
        )

        st.rerun()
