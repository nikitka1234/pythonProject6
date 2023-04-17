from flask import Flask, render_template


app = Flask(__name__)

news_list = [
    {"title": "Новость 1", "text": "текст для ноовости 1"},
    {"title": "Новость 2", "text": "тasdkasgfniuahg"},
    {"title": "Новость 3", "text": "тasdkasgf3246ergysdfgSGniuahg"}
]


def index():
    return render_template("index.html", news_list=news_list)


def news():
    return "Новости"


def news_detail(id):
    return render_template("news_detail.html", news_d=news_list[id])


def category(name):
    return f"Категория {name}"


app.add_url_rule('/', 'index', index)
app.add_url_rule('/news', 'news', news)
app.add_url_rule('/news_detail/<int:id>', 'news_detail', news_detail)
app.add_url_rule('/category/<string:name>', 'category', category)
