import json

def build_prompt(ticket):
    return f"Ticket: {ticket['message']}"

def draft_reply(ticket):
    msg = ticket['message'].lower()
    if "delay" in msg or "late" in msg:
        tone = "friendly"
        subject = "Re: Delivery delay"
    elif "refund" in msg or "money" in msg:
        tone = "firm"
        subject = "Re: Refund request"
    else:
        tone = "friendly"
        subject = "Re: Your request"
    
    return {
        "subject": subject,
        "body": f"Hi, thanks for telling us. We checked your issue: {ticket['message']} We will fix it soon.",
        "tone": tone
    }
