import json
from prompt_template import build_prompt

with open("sample_tickets.json", "r") as file:
    tickets = json.load(file)

for ticket in tickets:
    prompt = build_prompt(
        ticket["customer"],
        ticket["message"]
    )

    print(prompt)
