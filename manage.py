from flask import Flask
from flask import render_template
from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yoursupersecretkey'

class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/login')
def login():
	form = LoginForm()
	return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
