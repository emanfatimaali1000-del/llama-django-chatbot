
import requests


OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL_NAME = "llama3.2:1b"


def generate_response(conversation_history):

    try:

        messages = [
            {
                "role": "system",
                "content": (
                    "You are Llama, a helpful AI assistant. "
                    "Give accurate, friendly and well-organized answers. "
                    "Remember the conversation context and answer "
                    "follow-up questions accordingly. "
                    "If you don't know something, be honest."
                )
            }
        ]

        messages.extend(conversation_history)

        data = {
            "model": MODEL_NAME,
            "messages": messages,
            "stream": False
        }

        response = requests.post(
            OLLAMA_URL,
            json=data,
            timeout=180
        )

        response.raise_for_status()

        result = response.json()

        return result["message"]["content"]

    except requests.exceptions.ConnectionError:
        return "Error: Ollama is not running."

    except requests.exceptions.Timeout:
        return "Error: AI response timed out."

    except requests.exceptions.RequestException as e:
        return f"Error connecting to Ollama: {str(e)}"
