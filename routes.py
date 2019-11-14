from flask import Flask, render_template, request
from forms import ContactForm
from flask_mail import Message, Mail

mail = Mail()

app = Flask(__name__)

# anything that requires encryption needs this
# source: https://stackoverflow.com/questions/22463939/demystify-flask-app-secret-key
# source: https://stackoverflow.com/questions/34902378/where-do-i-get-a-secret-key-for-flask/34903502
app.secret_key = 'the random string'

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True

# this is the base email that will send the email to our client
# should import it from another file for increased security
app.config["MAIL_USERNAME"] = 'te816775@gmail.com'
app.config["MAIL_PASSWORD"] = 'Test123test'

mail.init_app(app)

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/quiz02', methods=['GET', 'POST'])
def quiz():
  form = ContactForm()

  if form.validate_on_submit():
    print (form.question01.data)
    print (form.question02.data)
    print (form.question03.data)
    print (form.question04.data)
    print (form.question05.data)
    print (form.question06.data)
    print (form.question07.data)
    print (form.question08.data)
    print (form.question09.data)
    print (form.question10.data)
  else:
    print (form.errors)

  if request.method == 'POST':
      # change the recipient to our clients email
      msg = Message(subject = "Quiz Result", sender='contact@example.com', recipients=['pivehe4516@resmail24.com'])
      # "%s" will convert argument to string
      msg.body = """
      From: Quiz Bot - user:
      The quiz result is as follows:
      %s
      %s
      %s
      %s
      %s
      %s
      %s
      %s
      %s
      %s
      """ % (form.question01.data, form.question02.data, form.question03.data, form.question04.data, form.question05.data, form.question06.data, form.question07.data, form.question08.data, form.question09.data, form.question10.data)
      mail.send(msg)

      return render_template('quiz02.html', success=True)

  elif request.method == 'GET':
    return render_template('quiz02.html', form=form)
  
if __name__ == '__main__':
  app.run(debug=True)
