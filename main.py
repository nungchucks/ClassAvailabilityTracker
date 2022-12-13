import requests
import smtplib
from bs4 import BeautifulSoup

# Target URL
url = ''

# Class you want to target
selector = 'dddefault'

# Create a previous value
prev_value = ''

# Make a request to  website
response = requests.get(url)

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Get a list of all elements of specific class
elements = soup.find_all("", class_=selector)

prev_class_4 = elements[3]

for i, element in enumerate(elements):
    if i == 3:
        if element != prev_class_4:
            print("Class 4 has changed!")
            prev_class_4 = element

# Set email and password
username = "your_email"
password = ""

# Set to email
to_email = "recipient_email"

# Create an SMTP object
smtp = smtplib.SMTP('smtp_server', port_number)

# Connect to the SMTP server
smtp.starttls()
smtp.login(username, password)

# Set the sender and recipient of the email
sender = username
recipient = to_email

# Set the subject and body of the email
subject = ""
body = ""

# Format the email message
msg = f"Subject: {subject}\n\n{body}"

# Send the email
smtp.sendmail(sender, recipient, msg)
smtp.quit()
