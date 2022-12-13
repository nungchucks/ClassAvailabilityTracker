import time

import requests
from bs4 import BeautifulSoup

# Set the URL of the website you want to monitor
url = 'https://owlexpress.kennesaw.edu/prodban/bwckschd.p_disp_detail_sched?term_in=202301&crn_in=15228'

# Set the CSS selector for the element you want to monitor
selector = '.dddefault'

# Set the initial value of the element
prev_value = ''

counter = 0

while True:
    # Make a request to the website
    response = requests.get(url)

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Get the value of the element using the CSS selector
    element = soup.select_one(selector)
    if element:
        value = element.text

    # Check if the value has changed
    if value != prev_value:
        # Print the new value
        print(value+"one")
        # Update the previous value
        prev_value = value

    time.sleep(5)

