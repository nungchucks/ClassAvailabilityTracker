## ClassAvailabilityTracker 👩‍🏫🔎
Tired of having to constantly check your school's website to see if a spot has opened up in a class? This simple python script will do it for you! 

Simply enter the URL of the course you would like to track, the name of the HTML class  storing the number of spots open, and you will get an email notifying you whenever that element's value changes. 

This will require you to have a SMTP server (smtp2go.com provides up to 1,000 emails for free). 

## Customizations: 

Feel free to change the find_all() selector to find() according to your needs. 
Also, the if statement can be changed according to the specific element that you wish to track.  
Finally, you can change the timer.sleep() count to whatever interval you would like the script to check the webpage for a change. 

Overall, the entire script should feel fairly intutive, but feel free to reach out with any questions -> nungchucks@gmail.com
