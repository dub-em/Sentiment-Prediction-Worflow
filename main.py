import smtplib, requests, os
from email.message import EmailMessage

def app():
    '''Function for triggering the prediction API and forwarding 
    an indication of successful operation to a personal email.'''
    msg = EmailMessage()

    msg['Subject'] = 'Update on Daily Prediction'
    msg['From'] = os.environ["EMAIL_ADDRESS"]
    msg['To'] = "michaeligbomezie@gmail.com"

    response = requests.get("https://research-questions-api.herokuapp.com/generaltrends/limit?limit=1")
    message = response.json()
    #msg.set_content(message["tweet"])
    msg.set_content("Tweet Extracted!")

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(os.environ["EMAIL_ADDRESS"], os.environ["EMAIL_PASSWORD"])
        smtp.send_message(msg)

    print("Daily Prediction Sucessful!")


app()


