from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

class GroqLLM:
    def __init__(self):
        load_dotenv(override=True)

    def get_llm(self):
        groq_api_key = os.getenv("GROQ_API_KEY")
        if not groq_api_key or groq_api_key == "your_groq_api_key_here":
            raise ValueError(
                "GROQ_API_KEY is missing. Add your real Groq API key to .env."
            )

        return ChatGroq(
            api_key=groq_api_key,
            model="openai/gpt-oss-20b",
        )