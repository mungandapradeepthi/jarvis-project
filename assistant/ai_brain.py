import ollama


chat_history = []


SYSTEM_PROMPT = """
You are Jarvis, a futuristic AI assistant.

Rules:
- Speak naturally like ChatGPT.
- Keep casual replies short.
- Give detailed answers only when needed.
- Do not generate random lists.
- Stay focused on the user's question.
- Sound smart and human-like.
- Avoid unnecessary explanations.
"""


def ask_ai(prompt):

    global chat_history

    try:

        chat_history.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ] + chat_history[-6:]

        response = ollama.chat(
            model="tinyllama",
            messages=messages
        )

        reply = response["message"]["content"]

        

        chat_history.append(
            {
                "role": "assistant",
                "content": reply
            }
        )

        return reply

    except Exception as e:

        return f"AI Error: {e}"