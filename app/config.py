from app.services.llm import OllamaProvider, GroqProvider, LLMService

llm_service = LLMService([
    GroqProvider("llama-3.3-70b-versatile"),
    OllamaProvider("qwen2.5:7b"),
])

router_llm_service = LLMService([
    GroqProvider("llama-3.1-8b-instant"),
    OllamaProvider("qwen2.5:3b"),
])