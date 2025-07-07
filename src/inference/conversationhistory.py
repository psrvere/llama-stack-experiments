import asyncio
from llama_stack_client import LlamaStackClient
from termcolor import cprint
from src.env import HOST, PORT, MODEL_NAME

client = LlamaStackClient(base_url=f'http://{HOST}:{PORT}')

async def chat_loop():
    conversation_history = []
    while True:
        user_input = input('User> ')
        if user_input.lower() in ['exit', 'quit', 'bye']:
            cprint('Ending conversation. Goodbye!', 'yellow')
            break

        user_message = {"role": "user", "content": user_input}
        conversation_history.append(user_message)

        response = client.inference.chat_completion(
            messages=conversation_history,
            model_id=MODEL_NAME,
        )
        cprint(f'> Response: {response.completion_message.content}', 'cyan')

        # Append the assistant message with all required fields
        assistant_message = {
            "role": "user",
            "content": response.completion_message.content,
            # Add any additional required fields here if necessary
        }
        conversation_history.append(assistant_message)

asyncio.run(chat_loop())