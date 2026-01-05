from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser

def get_rag_chain(llm):
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a helpful assistant. "
                "Answer ONLY using the provided context. "
                "If the answer is not in the context, say you don't know."
            ),
            MessagesPlaceholder(variable_name="history"),
            ("human", "Context:\n{context}\n\nQuestion:\n{question}")
        ]
    )

    return prompt | llm | StrOutputParser()
