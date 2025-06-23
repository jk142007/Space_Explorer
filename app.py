from flask import Flask
from flask_mail import Mail
from Blueprint.routes import main

app = Flask(__name__)
app.register_blueprint(main)

# Secret key for flash messages
app.secret_key = 'your_secret_key'

# Flask-Mail Configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'jambukiyakhushali@gmail.com'  # your email
app.config['MAIL_PASSWORD'] = 'mucvszvoqctshxel'     # your app password
app.config['MAIL_DEFAULT_SENDER'] = 'jambukiyakhushali@gmail.com'

# Initialize Mail
mail = Mail(app)
app.extensions['mail'] = mail  # So you can access it inside Blueprint using current_app.extensions

if __name__ == '__main__':
    app.run(debug=True)
