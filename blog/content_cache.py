import os

import markdown

from config.base import BASE_DIR


class ContentCache:

    def __init__(self):
        self.content_dir = os.path.join(BASE_DIR, 'blog/content')
        self.cache = {}

    def get(self, year, month, day, slug):
        full_path = os.path.join(
            self.content_dir,
            f'{year:04d}', f'{month:02d}', f'{day:02d}', f'{slug}.md'
        )
        try:
            content = self.cache[full_path]
        except KeyError:
            try:
                with open(full_path, 'r') as f:
                    content = f.read()
                    content = markdown.markdown(
                        content,
                        extensions=[
                            'markdown.extensions.fenced_code',
                            'markdown.extensions.tables',
                        ]
                    )
                self.cache[full_path] = content
            except FileNotFoundError:
                return '<h3>Not Found. I am sorry.</h3>'
        return content


content_cache = ContentCache()
