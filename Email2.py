import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

def send_email(sender_email, sender_password, recipient_email, subject, message, image_path):
    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Attach the message
    msg.attach(MIMEText(message, 'plain'))

    # Read the image file
    with open(image_path, 'rb') as img_file:
        # Create an image attachment
        img = MIMEImage(img_file.read())

    # Add the image attachment to the message
    msg.attach(img)

    # Connect to the SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)  # Update with your SMTP server details
    server.starttls()
    server.login(sender_email, sender_password)

    # Send the email
    server.send_message(msg)
    server.quit()

# Usage example
sender_email = 'boesmanman6@gmail.com'
sender_password = 'xgfj wugy upvm jfnj'
recipient_email = 'chadinhagiovanni7@gmail.com'
subject = 'Oi'
message = 'Fok jou'
image_path = r'C:\Users\stefa\OneDrive\Pictures\Screenshots\Screenshot 2023-07-05 172710.png'
for i in range(1 ,121 ):
    send_email(sender_email, sender_password, recipient_email, subject, message, image_path)

print("Done!")

