from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, EmailField
from wtforms.validators import DataRequired, Optional, Length


class UserForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired(message="Поле не должо быть пустым")])
    text = TextAreaField('Отзыв', validators=[DataRequired(message="Поле не должо быть пустым")])
    email = EmailField('Почта', validators=[Optional()])
    rating = SelectField('Оценка', choices=[1, 2, 3, 4, 5], default=5)
    submit = SubmitField('Отправить')


class NewNews(FlaskForm):
    title = StringField('Название новости', validators=[DataRequired(message="Поле не должо быть пустым"),
                                                        Length(max=255, message="Название не должно быть более 255 символов")])
    text = TextAreaField('Текст новости', validators=[DataRequired(message="Поле не должо быть пустым")])
    category = SelectField('Категория новости')
    submit = SubmitField('Отправить')