from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI

def get_llm(
    provider: str,
    api_key: str,
    model: str,
    temperature: float,
    max_tokens: int,
):
    if provider == "OpenAI":
        return ChatOpenAI(
            api_key=api_key,
            model=model,
            temperature=temperature,
            max_tokens=max_tokens,
        )

    # Default: Free LLM (Groq)
    return ChatGroq(
        api_key=api_key,
        model_name=model,
        temperature=temperature,
        max_tokens=max_tokens,
    )
