import time
import requests
import smtplib
from bs4 import BeautifulSoup

# Set the URL of the website you want to monitor
url = ''

# Set the CSS selector for the element you want to monitor
selector = 'dddefault'

# Set the initial value of the element
prev_value = '0'

# Make a request to the website
response = requests.get(url)

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Get a list of all elements with the specified class
elements = soup.find_all("td", class_=selector)

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

# Set email and password
username = "your_email"
# Format the email message
msg = f"Subject: {subject}\n\n{body}"

# Send the email
smtp.sendmail(sender, recipient, msg)
smtp.quit()

while True:
    # Make a request to the website
    response = requests.get(url)

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Get a list of all elements with the specified class
    elements = soup.find_all("td", class_=selector)

    # Check if the value of the third element has changed
    if elements[3].text != prev_value:
        # Update the previous value
        prev_value = elements[3].text
        smtp.sendmail(sender, recipient, msg)
        smtp.quit()
        break

    else:
        time.sleep(5)
        continue
