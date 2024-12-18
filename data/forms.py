from flask_wtf import FlaskForm
import wtforms


class SignUpForm(FlaskForm):
    username = wtforms.StringField("Введіть Логін", validators=[wtforms.validators.DataRequired])
    email = wtforms.EmailField("Введіть email", validators=[wtforms.validators.DataRequired(), wtforms.validators.Email()])
    password = wtforms.PasswordField("Введіть пароль", validators=[wtforms.validators.DataRequired(), wtforms.validators.length(6)])
    submit = wtforms.SubmitField("ОК")


class LoginForm(FlaskForm):
    username = wtforms.StringField("Введіть Логін або email", validators=[wtforms.validators.DataRequired])
    password = wtforms.PasswordField("Парол", validators=[wtforms.validators.DataRequired()])
    submit = wtforms.SubmitField("ОК")


