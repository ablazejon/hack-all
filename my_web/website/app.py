from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'ablaze.coder@proton.me'
app.config['MAIL_PASSWORD'] = 'ablaze_pro'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route('/')
def index():
    return render_template('services.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']

    msg = Message('Hacking Service', sender='ablaze.coder@proton.me', recipients=[email])
    msg.body = f'Hello {name},\n\nThank you for submitting your information. We will connect with you in 24 hours.'
    mail.send(msg)

    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)