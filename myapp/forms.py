# Forms for user registration and login, including validation
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FieldList, Form, FormField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from .models import User  # Needed for duplicate checks

class RegistrationForm(FlaskForm):
    # Fields for registration
    #email = StringField('Email', validators=[DataRequired(), Email(), Length(max=120)])
    username = StringField('Username', validators=[DataRequired(), Length(3, 20)])
    email = StringField('Email', validators=[DataRequired(), Length(3, 50)])
    password = PasswordField('Password', validators=[DataRequired(), Length(6, 30)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    # Custom validator for email uniqueness
    def validate_email(self, email):
        if User.query.filter_by(email=email.data).first():
            raise ValidationError('Email already registered.')

    # Custom validator for username uniqueness
    def validate_username(self, username):
        if User.query.filter_by(username=username.data).first():
            raise ValidationError('Username already taken.')

class LoginForm(FlaskForm):
    # Login form fields
    username = StringField('Username', validators=[DataRequired(), Length(3, 20)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class QuestionForm(Form):
    question = StringField("Question", validators=[DataRequired(), Length(0, 200)])
    answer = StringField("Answer", validators=[DataRequired(), Length(0, 50)])

class QuizCreationForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(3, 100)])
    questions = FieldList(FormField(QuestionForm), min_entries=1, max_entries=100)
    submit = SubmitField("Submit")
    
