import json


class JSONDatabase:

    def __init__(self):
        self.db_path = './content/posts.json'
        self.posts = []

    def load(self):
        with open(self.db_path, 'r') as f:
            self.posts = json.loads(f.read())


json_database = JSONDatabase()
