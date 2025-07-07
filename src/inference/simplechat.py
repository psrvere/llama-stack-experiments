from llama_stack_client import LlamaStackClient
from src.env import HOST, PORT, MODEL_NAME

client = LlamaStackClient(base_url=f'http://{HOST}:{PORT}')

response = client.inference.chat_completion(
    messages=[
        {"role": "system", "content": "You are a friendly assistant."},
        {"role": "user", "content": "Write a two-sentence poem about llama."}
    ],
    model_id=MODEL_NAME,
)

print(response.completion_message.content)