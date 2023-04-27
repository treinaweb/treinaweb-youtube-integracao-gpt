import requests

from django.conf import settings

from .models import Message

class GptService:
    def __init__(self):
        self.__model = settings.GPT_MODEL
        self.__open_ai_api_key = settings.OPEN_AI_API_KEY
        self.__open_ai_base_url = settings.OPEN_AI_BASE_URL

    def get_chat_message(self, messages):
        payload = {
            "model": self.__model,
            "messages": [self.__convert_to_chat_message_format(message) for message in messages]
        }
        headers = {
            "Authorization": f"Bearer {self.__open_ai_api_key}"
        }
        response = requests.post(
            f"{self.__open_ai_base_url}/chat/completions",
            json=payload,
            headers=headers,
        )
        body = response.json()
        return Message(role="assistant", content=body["choices"][0]["message"]["content"])

    def __convert_to_chat_message_format(self, message):
        return {
            "role": message.role,
            "content": message.content
        }