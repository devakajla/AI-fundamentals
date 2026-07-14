import json
from groq import Groq
from dotenv import load_dotenv
import os
from pydantic import BaseModel

load_dotenv()
my_api=os.getenv("GROQ_API_KEY")
client=Groq(api_key=my_api)

if not my_api:
    raise TypeError("API not found")

model="llama-3.3-70b-versatile"

        # text = """Hello, my name is Pratyush. I purchased an iPhone which stopped working.
        # My address is Delhi. Please contact me on abc@gmail.com. Regards, Pratyush."""

        # prompt=f"""This is a custom ticket, please extract information from this {text}"""

        # messages=[{
        #     "role":"system",
        #     "content":prompt
        # },
        # {
        #     "role":"user",
        #     "content":text
        # }]

        # response=client.chat.completions.create(
        #     model=model,
        #     messages=messages
        # )

        # print(response.choices[0].message.content)


text = """Hello, my name is Pratyush. I purchased an iPhone which stopped working.
        # My address is Delhi. Please contact me on abc@gmail.com. Regards, Pratyush."""

class Ticket(BaseModel):
    name:str
    email:str
    issue:str

schema = Ticket.model_json_schema()

response_format={
    "type":"json_object"
}

user_prompt=f"This is a custom ticket, please extract information from this {text}"

system_prompt=f"Extract info from {text} but only return based in json type {schema}"
message_system={
    "role":"system",
    "content":system_prompt
}

message_user={
    "role":"user",
    "content":user_prompt
}
messages=[message_system,message_user]

response=client.chat.completions.create(model=model, messages=messages, response_format=response_format)
answer=response.choices[0].message.content
print(response.choices[0].message.content)



# how to send to next chat model
raw_json=answer
data_file=json.loads(raw_json)
ticket=Ticket(**data_file)
print(ticket.name)
print(ticket.email)
print(ticket.issue)