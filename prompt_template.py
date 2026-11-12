def build_prompt(customer_name, customer_message):
    return f"""
You are a professional customer support agent.

Customer Name: {customer_name}

Customer Query:
{customer_message}

Write a polite and professional response.
"""
