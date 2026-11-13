import json, sys
from prompt_template import draft_reply

with open(sys.argv[1]) as f:
    ticket = json.load(f)

result = draft_reply(ticket)
print(json.dumps(result))
