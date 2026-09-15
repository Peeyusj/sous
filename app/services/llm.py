from langchain_ollama import ChatOllama
from langchain_groq import ChatGroq


class OllamaProvider:
    def __init__(self, model_name):
        self.client = ChatOllama(model=model_name)

    def run(self, messages):
        reply = self.client.invoke(messages)
        return reply.content

class GroqProvider:
    def __init__(self, model_name):
        self.client = ChatGroq(model=model_name)

    def run(self, messages):
        reply = self.client.invoke(messages)
        return reply.content


class LLMService:
    def __init__(self, providers):
        self.providers = providers

    def run(self, messages):
        for provider in self.providers:
            try:
                return provider.run(messages)
            except Exception as e:
                print(f"{provider.__class__.__name__} failed: {e}")

        raise RuntimeError("All LLM providers failed")