import json
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def build_prompt(ticket):
    return f"""
You are a support agent. Write a reply for this ticket.
Ticket: {ticket['message']}
Return ONLY JSON like this:
{{"subject": "...", "body": "...", "tone": "friendly"}}
"""

def draft_reply(ticket):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": build_prompt(ticket)}],
        response_format={"type": "json_object"}
    )
    return json.loads(response.choices[0].message.content)
