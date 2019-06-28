from sanic import Sanic
from sanic_jinja2 import SanicJinja2

from content_cache import content_cache
from jsondb import json_database

app = Sanic(__name__)

# Serves files from the static folder to the URL /static
app.static('/static', './static')
app.static('/favicon.ico', './static/favicon.ico')

jinja = SanicJinja2(app)
json_database.load()


BLOG_SETTINGS = {
    'title': 'sample.blog',
    'subtitle': 'this blog is about something',
    'blog_header': 'blog',
}


@app.route('/')
@jinja.template('index.html')
async def index(request):
    return {
        'db': json_database.posts['posts'],
        'settings': BLOG_SETTINGS
    }


@app.route('/<year:int>/<month:int>/<day:int>/<slug>/')
@jinja.template('post.html')
async def post(request, year, month, day, slug):
    content = content_cache.get(slug)
    try:
        post = [post for post in json_database.posts['posts'] if post['slug'] == slug][0]
        print(post['date'], f"{year}/{month}/{day}")
        if post['date'] != f"{year:04d}/{month:02d}/{day:02d}":
            content = '<h3>Not Found. I am sorry.</h3>'
    except IndexError:
        content = '<h3>Not Found. I am sorry.</h3>'
    return {
        'post': content,
        'settings': BLOG_SETTINGS
    }


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
