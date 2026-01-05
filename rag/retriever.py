def get_relevant_docs(vectorstore, query, k=4):
    retriever = vectorstore.as_retriever(
        search_kwargs={"k": k}
    )
    return retriever.invoke(query)
