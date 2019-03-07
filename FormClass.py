from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,FileField
from wtforms.validators import DataRequired

class NameForm(FlaskForm):
    name = StringField("What is your name :?",validators=[DataRequired()])
    file = FileField("upload file is :",validators=[DataRequired()])
    submit = SubmitField("提交")