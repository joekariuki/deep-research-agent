import os
from typing import Dict

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from agents import Agent, function_tool

EMAIL_FROM = os.environ.get("EMAIL_FROM")
EMAIL_TO = os.environ.get("EMAIL_TO")
SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")

@function_tool
def send_email(subject: str, html_body: str) -> Dict[str, str]:
    """
    Send an email with the given subject and HTML body.
    """
    # Check if the environment variables are set
    if not SENDGRID_API_KEY:
        raise ValueError("SENDGRID_API_KEY environment variable is not set")
    if not EMAIL_FROM:
        raise ValueError("EMAIL_FROM environment variable is not set")
    if not EMAIL_TO:
        raise ValueError("EMAIL_TO environment variable is not set")
    
    sg = SendGridAPIClient(api_key=SENDGRID_API_KEY)
    
    message = Mail(
        from_email=EMAIL_FROM,
        to_emails=EMAIL_TO,
        subject=subject,
        html_content=html_body
    )
    
    response = sg.send(message)
    print("Email response:", response.status_code)
    return {"status": "success"}


instructions = """You are able to send a nicely formatted HTML email based on a detailed report.
You will be provided with a detailed report. You should use your tool to send one email, providing the 
report converted into clean, well presented HTML with an appropriate subject line."""


email_agent = Agent(
    name="Email Agent",
    instructions=instructions,
    tools=[send_email],
    model=("gpt-5-mini"),
)