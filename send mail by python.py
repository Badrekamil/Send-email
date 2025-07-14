import smtplib
from email.message import EmailMessage

# Your Gmail credentials (DO NOT use your regular Gmail password)
sender_email = "kamilalikhan554@gmail.com"
app_password = "enter your app password"
receiver_email = "iarbazkhan47@gmail.com"

# Create the email
msg = EmailMessage()
msg['Subject'] = 'Task Completed – Python Email'
msg['From'] = sender_email
msg['To'] = receiver_email
msg.set_content("Hello! This is a test email sent using Python's smtplib with App Password.")

# Send the email
try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender_email, app_password)
        smtp.send_message(msg)
    print("✅ Email sent successfully to", receiver_email)
except Exception as e:
    print("❌ Error sending email:", e)
