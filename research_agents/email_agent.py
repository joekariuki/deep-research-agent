import os
from typing import Dict

import sendgrid
from sendgrid.helpers.mail import Email, Mail, Content, To
from agents import Agent, function_tool

@function_tool
def send_email(subject: str, html_body: str) -> Dict[str, str]:
    """
    Send an email with the given subject and HTML body.
    """
    sendgrid_api_key = os.environ.get('SENDGRID_API_KEY')
    email_from = os.environ.get('EMAIL_FROM')
    email_to = os.environ.get('EMAIL_TO')
    
    if not sendgrid_api_key:
        raise ValueError("SENDGRID_API_KEY environment variable is not set")
    
    sg = sendgrid.SendGridAPIClient(api_key=sendgrid_api_key)
    from_email = Email(email_from)
    to_email = To(email_to)
    content = Content("text/html", html_body)
    mail = Mail(from_email, to_email, subject, content).get()
    
    response = sg.client.mail.send.post(request_body=mail)
    print("Email response:", response.status_code)
    return {"status": "success"}


instructions = """You are able to send a nicely formatted HTML email based on a detailed report.
You will be provided with a detailed report. You should use your tool to send one email, providing the 
report converted into clean, well presented HTML with an appropriate subject line."""


email_agent = Agent(
    name="Email Agent",
    instructions=instructions,
    tools=[send_email],
    model="gpt-5-mini",
)