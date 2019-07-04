import os

from sanic import Sanic
from sanic_jinja2 import SanicJinja2

from config.base import BASE_DIR, BLOG_SETTINGS
from blog.content_cache import content_cache
from blog.jsondb import json_database


def create_app(**kwargs):
    return Sanic(__name__)


app = create_app()

# Serves files from the static folder to the URL /static
app.static('/static', os.path.join(BASE_DIR, 'static'),
           use_modified_since=True)
app.static('/resources', os.path.join(BASE_DIR, 'blog/content/resources'),
           use_modified_since=True)
app.static('/favicon.ico', os.path.join(BASE_DIR, 'static/favicon.ico'))

jinja = SanicJinja2(app)
json_database.load()


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
    content = content_cache.get(year, month, day, slug)
    return {
        'post': content,
        'settings': BLOG_SETTINGS
    }


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)  # nosec
