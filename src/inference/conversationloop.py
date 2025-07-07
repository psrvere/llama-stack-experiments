import asyncio
from llama_stack_client import LlamaStackClient
from termcolor import cprint
from src.env import HOST, PORT, MODEL_NAME

client = LlamaStackClient(base_url=f'http://{HOST}:{PORT}')

async def chat_loop():
    while True:
        user_input = input('User> ')
        if user_input.lower() in ['exit', 'quit', 'bye']:
            cprint('Ending conversation. Goodbye!', 'yellow')
            break

        message = {"role": "user", "content": user_input}
        response = client.inference.chat_completion(
            messages=[message],
            model_id=MODEL_NAME
        )
        cprint(f'> Response: {response.completion_message.content}', 'cyan')

asyncio.run(chat_loop())