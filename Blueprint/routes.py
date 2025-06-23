from flask import render_template, request, redirect, url_for, flash, current_app
from Blueprint import main
from flask_mail import Mail, Message

@main.route('/')
@main.route('/home')
def home():
    return render_template('home.html')

@main.route('/resources')
def resources():
    return render_template('resources.html')

@main.route('/learn')
def learn():
    return render_template('learn.html')

@main.route('/about', methods=['GET', 'POST'])
def about():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        mail = current_app.extensions.get('mail')
        if mail:
            msg = Message(subject=f"Contact Form from {name}",
                          recipients=['jambukiyakhushali@gmail.com'],  # <-- replace with your email
                          body=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}")
            mail.send(msg)

            flash("Thank you for contacting us!", "success")
        else:
            flash("Mail server not configured.", "danger")

        return redirect(url_for('main.about'))

    return render_template('about.html')

@main.route('/solarsys')
def solarsys():
    return render_template('solarsys.html')

@main.route('/galaxy')
def galaxy():
    return render_template('galaxy.html')

@main.route('/blackhole')
def blackhole():
    return render_template('blackhole.html')
