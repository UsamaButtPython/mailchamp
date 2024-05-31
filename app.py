from flask import Flask

app = Flask(__name__)



from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
mail= Mail(app)

app.config['MAIL_SERVER']='smtp.mandrillapp.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'info@phonepayinc.com'
app.config['MAIL_PASSWORD'] = 'n8dvJCao1FPorBFyYFGEkg'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)

@app.route("/")
def index():
   msg = Message('Hello', sender = 'info@phonepayinc.com', recipients = ['testmail@yopmail.com'])
   msg.body = "Hello Flask message sent from Flask-Mail"
   mail.send(msg)
   return "Sent"

if __name__ == '__main__':
   app.run(debug = True)







# import mailchimp_transactional as MailchimpTransactional
# from mailchimp_transactional.api_client import ApiClientError

# mailchimp = MailchimpTransactional.Client('n8dvJCao1FPorBFyYFGEkg')
# message = {
#     "from_email": "info@phonepayinc.com",
#     "subject": "Hello world",
#     "text": "Welcome to Mailchimp Transactional!",
#     "to": [
#       {
#         "email": "abdullah.us1721@gmail.com",
#         "type": "to"
#       }
#     ]
# }

# def run():
#   try:
#     response = mailchimp.messages.send({"message":message})
#     print('API called successfully: {}'.format(response))
#   except ApiClientError as error:
#     print('An exception occurred: {}'.format(error.text))

# @app.route('/')
# def Index():
#     run()

#     return 'Hello World from Python Flask!'






app.run(debug=True,host='0.0.0.0', port=5000)