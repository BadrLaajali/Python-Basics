import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
sender_email = "hrtsdi@freesmtpservers.com"  # Your email address
recipient_email = "lechatferu@gmail.com"  # Recipient's email address
subject = "Test Email"
message = "This is a test email sent using anonymous SMTP."

# Create the email message
msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = recipient_email
msg["Subject"] = subject
msg.attach(MIMEText(message, "plain"))

# SMTP server configuration
smtp_server = "smtp.freesmtpservers.com"
smtp_port = 25

try:
    # Connect to the SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)

    # Send the email
    server.sendmail(sender_email, recipient_email, msg.as_string())

    # Close the SMTP server connection
    server.quit()

    print("Email sent successfully!")

except Exception as e:
    print(f"An error occurred: {str(e)}")
