from flask import Flask, request, redirect, url_for, render_template
from flask_mail import Mail, Message
import os

app = Flask(__name__)

# =========================
# ROUTES (PAGES)
# =========================

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/talk_to_us')
def talk_to_us():
    return render_template('talk_to_us.html')


# MAIL CONFIG
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'Metachainsrecovery@gmail.com'
app.config['MAIL_PASSWORD'] = 'jtov bojk gjqn oizv'  # no spaces
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_DEFAULT_SENDER'] = app.config['MAIL_USERNAME']

mail = Mail(app)

# FORM SUBMISSION
@app.route('/submit-contact', methods=['POST'])
def submit_contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    msg = Message(
        subject=f"New Contact Message from {name}",
        recipients=[app.config['MAIL_USERNAME']],
        reply_to=email,
        body=f"""Name: {name}
Email: {email}

Message:
{message}
"""
    )

    try:
        mail.send(msg)
    except Exception as e:
        return f"Email error: {e}"

    return redirect(url_for('success'))

# SUCCESS PAGE
@app.route('/success')
def success():
    return render_template('sent.html')

if __name__ == '__main__':
    app.run(debug=True)

