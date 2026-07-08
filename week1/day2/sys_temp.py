import os
from pathlib import Path
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
my_api=os.getenv("GROQ_API_KEY")

if not my_api:
    raise ValueError("API Key not found")

client=Groq(api_key=my_api)

role1="system"
prompt1="You are my strict boss"

model="llama-3.3-70b-versatile"

message1={
    "role":role1,
    "content":prompt1
}

message2={
    "role":"user",
    "content":"I love you"
}

messages=[message1,message2]

response=client.chat.completions.create(
    model=model,messages=messages, temperature=2
)

print(response.choices[0].message.content)