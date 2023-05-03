from flask import render_template, redirect, url_for

from . import app, db
from .models import News, Category
from .forms import UserForm, NewNews


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
