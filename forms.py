# flask_wtf is an extension that allows you define form fields and render them using an HTML template
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import TextField, TextAreaField, SubmitField, RadioField

class ContactForm(FlaskForm):
  subject = TextField("Subject")
  message = TextAreaField("Message")
  submit = SubmitField("Send")
  question01 = RadioField('What is your answer to the 1st question?', choices = [('A','Adam'),('B','Bob'), ('C', 'Chris')])
  question02 = RadioField('What is your answer to the 2nd question?', choices = [('A','Adam'),('B','Bob'), ('C', 'Chris')])
  question03 = RadioField('What is your answer to the 3rd question?', choices = [('A','Adam'),('B','Bob'), ('C', 'Chris')])
  question04 = RadioField('What is your answer to the 4th question?', choices = [('A','Adam'),('B','Bob'), ('C', 'Chris')])
  question05 = RadioField('What is your answer to the 5th question?', choices = [('A','Adam'),('B','Bob'), ('C', 'Chris')])
  question06 = RadioField('What is your answer to the 6th question?', choices = [('A','Adam'),('B','Bob'), ('C', 'Chris')])
  question07 = RadioField('What is your answer to the 7th question?', choices = [('A','Adam'),('B','Bob'), ('C', 'Chris')])
  question08 = RadioField('What is your answer to the 8th question?', choices = [('A','Adam'),('B','Bob'), ('C', 'Chris')])
  question09 = RadioField('What is your answer to the 9th question?', choices = [('A','Adam'),('B','Bob'), ('C', 'Chris')])
  question10 = RadioField('What is your answer to the 10th question?', choices = [('A','Adam'),('B','Bob'), ('C', 'Chris')])
