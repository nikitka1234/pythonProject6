from flask import Flask, render_template, redirect

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, EmailField
from wtforms.validators import DataRequired, Optional, Length

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


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


app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET KEY'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

db = SQLAlchemy(app)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True, nullable=False)
    news = db.relationship('News', back_populates='category')

    def __repr__(self):
        return f"Category: {self.id}. {self.title}"


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True, nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow())
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True)
    category = db.relationship('Category', back_populates='news')

    def __repr__(self):
        return f"News: {self.id}. {self.title}"


with app.app_context():
    db.create_all()


def index():
    news_list = News.query.all()
    categories = Category.query.all()

    return render_template("index.html", news_list=news_list, categories=categories)


def form():
    user_form = UserForm()
    categories = Category.query.all()

    if user_form.validate_on_submit():
        name = user_form.name.data
        text = user_form.text.data
        email = user_form.email.data
        rating = user_form.rating.data

        print(name, text, email, rating, sep="\n--------------\n")

        return redirect("/")

    return render_template("form.html", form=user_form, categories=categories)


def add_news():
    new = NewNews()
    new.category.choices = [cat.title for cat in Category.query.all()]
    categories = Category.query.all()

    if new.validate_on_submit():
        no = News()
        no.title = new.title.data
        no.text = new.text.data
        no.category_id = Category.query.filter(Category.title == new.category.data).first().id
        db.session.add(no)
        db.session.commit()

        return redirect("/")

    return render_template("add_news.html", form=new, categories=categories)


def news():
    return "Новости"


def news_detail(id):
    news_d = News.query.get(id)
    categories = Category.query.all()

    return render_template("news_detail.html", news_d=news_d, categories=categories)


def category(id):
    c_news_list = News.query.filter(News.category_id == id).all()
    categories = Category.query.all()

    return render_template("category.html", category_name=Category.query.get(id).title,
                           news=c_news_list, categories=categories)


app.add_url_rule('/', 'index', index)
app.add_url_rule('/form', 'form', form, methods=["GET", "POST"])
app.add_url_rule('/add_news', 'add_news', add_news, methods=["GET", "POST"])
app.add_url_rule('/news', 'news', news)
app.add_url_rule('/news_detail/<int:id>', 'news_detail', news_detail)
app.add_url_rule('/category/<int:id>', 'category', category)
