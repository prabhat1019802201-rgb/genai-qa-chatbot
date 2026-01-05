from transformers import pipeline
from langchain_community.llms import HuggingFacePipeline
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq


def get_llm(
    provider: str,
    api_key: str | None,
    model: str,
    temperature: float,
    max_tokens: int,
):
    # -------------------------------
    # Hugging Face (Local, Free)
    # -------------------------------
    if provider == "HuggingFace (Local / Free)":
        pipe = pipeline(
            task="text-generation",
            model=model,
            max_new_tokens=max_tokens,
            temperature=temperature,
        )
        return HuggingFacePipeline(pipeline=pipe)

    # -------------------------------
    # Groq
    # -------------------------------
    if provider == "Groq":
        return ChatGroq(
            api_key=api_key,
            model_name=model,
            temperature=temperature,
            max_tokens=max_tokens,
        )

    # -------------------------------
    # OpenAI
    # -------------------------------
    if provider == "OpenAI":
        return ChatOpenAI(
            api_key=api_key,
            model=model,
            temperature=temperature,
            max_tokens=max_tokens,
        )

    raise ValueError(f"Unsupported provider: {provider}")
