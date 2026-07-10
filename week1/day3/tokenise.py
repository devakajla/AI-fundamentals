import os
from pathlib import Path
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
my_api=os.getenv("GROQ_API_KEY")

if not my_api:
    raise ValueError("API key not found")

client=Groq(api_key=my_api)

model="llama-3.3-70b-versatile"

role="user"
prompt1="Hi!"
prompt2="Explain time travel in detail"
prompt3="Write an elaborative guide on how to get life on routine if you feel no purpose and no motivation for life"

prompts=[prompt1,prompt2,prompt3]


for prompt in prompts:
    message={
    "role":role,
    "content":prompt
    }
    messgaes=[message]

    response=client.chat.completions.create(model=model, messages=messgaes, temperature=0.7, max_tokens=500)

    usage=response.usage

    print(f"Prompt token:{usage.prompt_tokens}")
    print(f"Completion token:{usage.completion_tokens}")
    print(f"Total tokens: {usage.prompt_tokens+usage.completion_tokens}")
    print(f"Reason for stopping: {response.choices[0].finish_reason}")

