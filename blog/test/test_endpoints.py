from app import app
from blog.jsondb import json_database


def test_index_returns_200():
    request, response = app.test_client.get('/')
    assert response.status == 200  # nosec


def test_index_put_not_allowed():
    json_database.load()
    assert json_database.posts['posts'] != []  # nosec
    for post in json_database.posts['posts']:
        url = f'/{post["date"]}/{post["slug"]}'
        request, response = app.test_client.get(url)
        assert response.status == 200  # nosec


def test_static_serving():
    request, response = app.test_client.get(
        '/static/js/clean-blog.js')
    assert response.status == 200  # nosec


def test_reources_serving():
    request, response = app.test_client.get(
        '/resources/sphinx/hacking-sphinx-01.png')
    assert response.status == 200  # nosec
