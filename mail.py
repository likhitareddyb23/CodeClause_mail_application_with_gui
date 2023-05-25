import tkinter as tk
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email():
    sender_email = "likhita@gmail.com"
    sender_password = "likhita"
    recipient_email = recipient_entry.get()
    subject = subject_entry.get()
    message = message_text.get("1.0", "end")

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg["Subject"] = subject
    msg.attach(MIMEText(message, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print("An error occurred while sending the email:", str(e))

# Create the GUI
root = tk.Tk()
root.title("Mail Application")

# Recipient Entry
recipient_label = tk.Label(root, text="Recipient:")
recipient_label.pack()
recipient_entry = tk.Entry(root)
recipient_entry.pack()

# Subject Entry
subject_label = tk.Label(root, text="Subject:")
subject_label.pack()
subject_entry = tk.Entry(root)
subject_entry.pack()

# Message Text
message_label = tk.Label(root, text="Message:")
message_label.pack()
message_text = tk.Text(root, height=10, width=50)
message_text.pack()

# Send Button
send_button = tk.Button(root, text="Send", command=send_email)
send_button.pack()

# Run the GUI
root.mainloop()
