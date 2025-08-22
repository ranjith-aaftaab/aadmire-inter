import logging
from flask import Flask, render_template, request, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'Admire Interiors'  # Update the secret key

# Flask-Mail Configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'ranjithpython072@gmail.com'  # Replace with your email
app.config['MAIL_PASSWORD'] = 'xstn jyzt audy bviw'  # Secure this with environment variable in production

mail = Mail(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/who_we_are')
def who_we_are():
    return render_template('who_we_are.html')

@app.route('/what_we_do')
def what_we_do():
    return render_template('what_we_do.html')

@app.route('/clients')
def clients():
    return render_template('clients.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        phone = request.form.get('phone')
        email = request.form.get('email')
        message = request.form.get('message')

        subject = "New Contact Form Submission - Admire Interiors"
        recipient = "ranjithmedigital@gmail.com"  # Replace with actual email
        cc_recipient = "ranjithg155@gmail.com"        # Optional CC

        message_body = f"Name: {name}\nPhone: {phone}\nEmail: {email}\nMessage: {message}"

        try:
            msg = Message(subject, sender=app.config['MAIL_USERNAME'], recipients=[recipient])
            msg.cc = [cc_recipient]
            msg.body = message_body
            mail.send(msg)
            flash("Email sent successfully!", "success")
            logging.info(f"Contact email sent from {name} to {recipient}.")
        except Exception as e:
            error_message = f"Failed to send email: {str(e)}"
            flash(error_message, "danger")
            logging.error(error_message)

    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)