from prompt_template import draft_reply
import json

with open("sample_tickets.json") as f:
    tickets = json.load(f)

def test_keys():
    for t in tickets[:3]:
        out = draft_reply(t)
        assert "subject" in out
        assert "body" in out
        assert "tone" in out
