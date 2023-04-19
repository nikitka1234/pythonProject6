from flask import Flask, render_template, redirect

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, EmailField
from wtforms.validators import DataRequired, Optional


class UserForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired(message="Поле не должо быть пустым")])
    text = TextAreaField('Отзыв', validators=[DataRequired(message="Поле не должо быть пустым")])
    email = EmailField('Почта', validators=[Optional()])
    rating = SelectField('Оценка', choices=[1, 2, 3, 4, 5], default=5)
    submit = SubmitField('Отправить')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET KEY'

news_list = [
    {"title": "Новость 1", "text": "текст для ноовости 1"},
    {"title": "Новость 2", "text": "тasdkasgfniuahg"},
    {"title": "Новость 3", "text": "тasdkasgf3246ergysdfgSGniuahg"}
]


def index():
    return render_template("index.html", news_list=news_list)


def form():
    user_form = UserForm()

    if user_form.validate_on_submit():
        name = user_form.name.data
        text = user_form.text.data
        email = user_form.email.data
        rating = user_form.rating.data

        print(name, text, email, rating, sep="\n--------------\n")

        return redirect("/")

    return render_template("form.html", form=user_form)


def news():
    return "Новости"


def news_detail(id):
    return render_template("news_detail.html", news_d=news_list[id])


def category(name):
    return f"Категория {name}"


app.add_url_rule('/', 'index', index)
app.add_url_rule('/form', 'form', form, methods=["GET", "POST"])
app.add_url_rule('/news', 'news', news)
app.add_url_rule('/news_detail/<int:id>', 'news_detail', news_detail)
app.add_url_rule('/category/<string:name>', 'category', category)
