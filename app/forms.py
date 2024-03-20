from flask_wtf import FlaskForm
from wtforms import FileField, StringField, PasswordField, TextAreaField, SelectField
from wtforms.validators import InputRequired
from flask_wtf.file import FileAllowed, FileRequired, FileField

class PropertyForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    numBedrooms= StringField('Number of bedrooms', validators=[InputRequired()])
    numBathrooms= StringField('Number of bathrooms', validators=[InputRequired()])
    location= StringField('Location', validators=[InputRequired()])
    price= StringField('Price', validators=[InputRequired()])
    pType= SelectField('Type', choices=[('house', 'House'), ('apartment', 'Apartment')], validators=[InputRequired()])
    desc= TextAreaField('description')
    photo = FileField('Photo', validators=[
    FileRequired(),
    FileAllowed(['jpg', 'png'], 'Images only!')])