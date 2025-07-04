# from flask import Flask, render_template, request, make_response, redirect, url_for, session

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html', username="Hemanth", items=['csgo', 'PUBG', 'Battlefield'])

# # Show form
# @app.route('/form')
# def home():
#     return render_template('submit.html')

# # Form submission
# @app.route('/submit', methods=['POST'])
# def submit():
#     username = request.form.get('username')
#     # Redirect to thank you page after POST
#     return redirect(url_for('thank_you', user=username))

# # Custom response
# @app.route('/response')
# def custom_response():
#     response = make_response(render_template('response.html'), 404)
#     response.headers['X-Custom-Header'] = 'Value'
#     return response

# # Thank you page after redirect
# @app.route('/thank-you')
# def thank_you():
#     user = request.args.get('user', 'Guest')
#     return f"Thanks for submitting, {user}!"

# # Session
# @app.route('/login', methods = ['POST'])
# def login():
#     session ['username'] = request.form.get("username")
#     return redirect(url_for('profile'))

# app.secret_key = 'your-secret-key'
# @app.route('/profile')
# def profile():
#     username = session.get('username', 'Guest')
#     return redirect(url_for('profile.html', username = username))

# # Form validation
# @app.route('/register', methods = ['GET', 'POST'])
# def register():
#     username = request.form.get('username')
#     email = request.form.get('email')
#     errors = []

#     if not username or len(username) < 3:
#         errors.append("Username must be at least 3 characters long")
#     if not email or '@' not in email:
#         errors.append('Valid email is required.')

#     if errors:
#         return render_template("register.html", errors = errors)
#     return render_template("success.html", username = username)


# # WTForms - A flask template to create forms
# from flask_wtf import FlaskForm
# from wtforms import StringField, PasswordField, SubmitField
# from wtforms.validators import DataRequired, Email, Length

# class LoginForm(FlaskForm):
#     email = StringField('Email', validators=[DataRequired(), Email()])
#     password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
#     submit = SubmitField('Login')

# from flask import Flask, render_template, redirect, url_for
# from Flask_new_app_2.forms import LoginForm

# app = Flask(__name__)
# app.secret_key = 'your_secret_key'  # Needed for CSRF protection

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         email = form.email.data
#         return render_template('login_success.html', email=email)
#     return render_template('login.html', form=form)

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request, make_response, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for CSRF protection

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Login')

@app.route('/')
def index():
    return render_template('index.html', username="Hemanth", items=['csgo', 'PUBG', 'Battlefield'])

# Show HTML form
@app.route('/form')
def home():
    return render_template('submit.html')

# Handle POST form
@app.route('/submit', methods=['POST'])
def submit():
    username = request.form.get('username')
    return redirect(url_for('thank_you', user=username))

# Thank-you after form POST
@app.route('/thank-you')
def thank_you():
    user = request.args.get('user', 'Guest')
    return f"Thanks for submitting, {user}!"

# Custom response with headers
@app.route('/response')
def custom_response():
    response = make_response(render_template('response.html'), 404)
    response.headers['X-Custom-Header'] = 'Value'
    return response

# Session login
@app.route('/session-login', methods=['POST'])
def session_login():
    session['username'] = request.form.get("username")
    return redirect(url_for('profile'))

@app.route('/profile')
def profile():
    username = session.get('username', 'Guest')
    return render_template('profile.html', username=username)

# Form validation manually
@app.route('/register', methods=['GET', 'POST'])
def register():
    errors = []
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')

        if not username or len(username) < 3:
            errors.append("Username must be at least 3 characters long")
        if not email or '@' not in email:
            errors.append("Valid email is required.")

        if errors:
            return render_template("register.html", errors=errors)
        return render_template("success.html", username=username)

    return render_template("register.html", errors=errors)

# WTForms-based login form
@app.route('/login-form', methods=['GET', 'POST'])
def login_form():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        return render_template('login_success.html', email=email)
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
