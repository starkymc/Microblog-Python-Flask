from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    BooleanField,
    SubmitField,
    TextAreaField
)
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    username = StringField("Nombre de usuario", validators=[DataRequired()])
    password = PasswordField("Contraseña", validators=[DataRequired()])
    remember_me = BooleanField("Recuérdame")
    submit = SubmitField("Ingresar")


class EditProfileForm(FlaskForm):
    name = StringField("Nombre real", validators=[Length(0, 64)])
    location = StringField("Locación", validators=[Length(0, 64)])
    about_me = TextAreaField("Sobre mi")
    submit = SubmitField("Actualizar Perfil")

class PostForm(FlaskForm):
    body = TextAreaField("¿En que estas pensando?", validators=[DataRequired()])
    submit = SubmitField("Postear")
