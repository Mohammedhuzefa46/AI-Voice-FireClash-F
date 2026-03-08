import ollama
from rag import retrieve_context

def generate_llm_response(user_text, emotion):

    context = retrieve_context(user_text)

    prompt = f"""
You are an AI support assistant.

User said: {user_text}

User emotion: {emotion}

Relevant knowledge:
{context}

Respond politely and helpfully.
"""

    response = ollama.chat(
        model="phi3",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]