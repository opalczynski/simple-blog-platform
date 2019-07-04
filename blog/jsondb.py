import json
import os

from config.base import BASE_DIR


class BaseJSONDatabase:
    content_dir = None
    store_attribute = None

    def __init__(self):
        self.db_path = os.path.join(
            BASE_DIR,
            self.content_dir
        )
        setattr(self, self.store_attribute, [])

    def load(self):
        with open(self.db_path, 'r') as f:
            setattr(self, self.store_attribute, json.loads(f.read()))


class JSONDatabase(BaseJSONDatabase):
    content_dir = 'blog/content/posts.json'
    store_attribute = 'posts'


json_database = JSONDatabase()
