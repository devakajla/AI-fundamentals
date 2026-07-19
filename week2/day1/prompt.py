from groq import Groq
from dotenv import load_dotenv
import os
from pathlib import Path

load_dotenv()
my_api=os.getenv("GROQ_API_KEY")
if not my_api:
    raise TypeError("API not found")

client=Groq(api_key=my_api)
model="llama-3.3-70b-versatile"

def llm_answer(prompt):
    message = {
        "role": "user",
        "content": prompt
    }
    messages = [message]

    response = client.chat.completions.create(
        model=model,
        messages=messages
    )

    answer = response.choices[0].message.content
    return answer

prompt = """
Role: You are a support assistant at a mobile/laptop company.
Task: You have to classify the issue into a category.
Constraint: You have to classify the issue in one of the three categories,
namely Billing, Technical, Return.
Output Format: Your answer should be in one word only. The one word should be
one of the categories given to you in constraints.
For instance, if he wants a refund then category is Return.
Fallback: If the issue is unrelated to any of the categories mentioned in
constraints, then the answer should be Other.

This is a user complaint: My laptop is not working.
"""

print(llm_answer(prompt))
# "My laptop is not working" -> Technical
# "My marriage is broken"    -> Other   (correctly caught by fallback)
