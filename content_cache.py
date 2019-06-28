import os

import markdown


class ContentCache:

    def __init__(self):
        self.content_dir = os.path.join('./content')
        self.cache = {}

    def get(self, slug):
        full_path = os.path.join(self.content_dir, f'{slug}.md')
        try:
            content = self.cache[full_path]
        except KeyError:
            try:
                with open(full_path, 'r') as f:
                    content = f.read()
                    content = markdown.markdown(content, extensions=['markdown.extensions.fenced_code'])
                self.cache[full_path] = content
            except FileNotFoundError:
                return '<h3>Not Found. I am sorry.</h3>'
        return content


content_cache = ContentCache()
