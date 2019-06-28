import os

import markdown


class ContentCache:

    def __init__(self):
        self.content_dir = os.path.join('./content')
        self.cache = {}

    def get(self, path):
        path = path.replace('.html', '.md')
        full_path = os.path.join(self.content_dir, path)
        try:
            content = self.cache[path]
        except KeyError:
            try:
                with open(full_path, 'r') as f:
                    content = f.read()
                    content = markdown.markdown(content, extensions=['markdown.extensions.fenced_code'])
                self.cache[full_path] = content
            except FileNotFoundError:
                return '<h3>Not Found. We are sorry.</h3>'
        return content


content_cache = ContentCache()
