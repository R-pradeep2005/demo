import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender_email, sender_password, recipient_email, subject, body):
    try:
        # Set up the MIME structure
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = recipient_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        # Connect to the Gmail server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()  # Secure the connection
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, recipient_email, message.as_string())
        server.quit()
        print("Email sent successfully!")

    except Exception as e:
        print(f"Failed to send email: {e}")

# Replace with your credentials
sender_email = "22cs091@kcgcollege.com"
sender_password = "tn51f6864"
recipient_email = "bocarno470@gmail.com"
subject = "Test Email"
body = "Hello! This is a test email sent from a Python script."

send_email(sender_email, sender_password, recipient_email, subject, body)
