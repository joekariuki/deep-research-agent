import os
from typing import Dict

import sendgrid
from sendgrid.helpers.mail import Mail, Email, Content, To
from agents import Agent, function_tool

EMAIL_FROM = os.environ.get("EMAIL_FROM")
EMAIL_TO = os.environ.get("EMAIL_TO")
SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")

@function_tool
def send_email(subject: str, html_body: str) -> Dict[str, str]:
    """
    Send an email with the given subject and HTML body.
    """
    sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)
    from_email = Email(EMAIL_FROM)
    to_email = To(EMAIL_TO)
    content = Content("text/html", html_body)
    mail = Mail(from_email, to_email, subject, content).get()
    response = sg.client.mail.send.post(request_body=mail)
    print("Email response:", response.status_code)
    return { "status": "success" }


instructions ="""You are able to send a nicely formatted HTML email based on a detailed report.
You will be provided with a detailed report. You should use your tool to send one email, providing the 
report converted into clean, well presented HTML with an appropriate subject line."""


email_agent = Agent(
    name="Email Agent",
    instructions=instructions,
    tools=[send_email],
    model=("gpt-5-mini"),
)