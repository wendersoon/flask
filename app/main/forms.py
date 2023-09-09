from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, Regexp

class NameForm(FlaskForm):
    name = StringField('Whats is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')
    
class EditProfileForm(FlaskForm):
    name = StringField('Real name', validators=[Length(0, 64)])
    location = StringField('Location', validators=[Length(0, 64)])
    about_me = TextAreaField('About me')
    submit = SubmitField('Submit')
    
class EditProfileAdminForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired() Length(1, 64),
                                             Email()])
    username = StringField('Username', validators=[
        DataRequired(), Length(1, 64),
        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, 'Usernames must have only letters, numbers, dots or ''underscores')])
    confirme