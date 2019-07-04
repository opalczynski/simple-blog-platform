# SIMPLE BLOG PLATFORM

## Why?

Literally - because I can.

I know that there are tons of solutions for handling blog, but I wanted to have mine :) 

## For who?

As this is really "bare" it is for developers who actually understands a bit of programming and services.
For sure not for 'normal' people from UI world.

Currently I am running a blog using this "platform": [showpy.tech](https://showpy.tech)

I am writing my new posts in the IDE, I am publishing new ones using fully set up bitbucket pipelines, it:

1. Builds new docker image
2. Push docker image to container registry
3. Later container is update on the running instance
4. Cache is invalidated (only the / and /reading-list*) paths - as this is the only one that change often.

The whole setup took me like couple of hours - including writing this README and the blog platform itself. 

## Benefits?

* No database
* No nothing - only this docker image

## How use it?

    docker-compose up -d

Go to http://localhost:8031

You should see samples posts.

```json
    {
      "title": "Sample Post",
      "slug": "sample-post",
      "date": "2019/07/04",
      "time": "15:49",
      "author": "Some Test",
      "intro": "And this is intro/subtitle"
    }
```

Posts are list there - so extend the list not replace.

Btw. I have no pagination yet - but who cares; only few of blogs has more than 100 posts.
Usually people lost enthusiasm lot earlier.

After changes - you need to rebuild image and restart application.
It can be very nicely incorporated into CI/CD - this what I am doing.


## To change bg image & configuration

Change the `static/img/home-bg.jpg` to whatever you like.
Same story with `favicon.ico` -> pyt there whatever you like.
To add image to your posts - add them under `static/img/posts` (you can organize this on your own);

There's an example of how to do it in `sample-post.md`.

In the `config/base.py` file you can find:

```python
BLOG_SETTINGS = {
    'title': 'sample.blog',
    'subtitle': 'everything you want to know',
}
```

You can change that - to meet your needs. It will be displayed on few places in the blog page,
the most important is of course the welcome text on you blog.

## How to add new page

Adding new page can be describe in 3 steps:

* You need too add new view handler like this:

```python
@app.route('/about/')
@jinja.template('about.html')
async def about(request):
    return {
        'settings': BLOG_SETTINGS
    }
```

in the `app.py` file.

* You need to add new template, simply create `about.html` file in `templates` 
directory. As we are using `jinja2` here, your template should look like this initially:

```html
{% extends 'base.html' %}

{% block content %}
  <p>Put some content here</p>
{% endblock %}
```

* Add new page to menu - whatever you like, but menu is a good first choice:

Go to `templates/base.html` file and there find `<!-- Navigation -->` comment,
few lines under you have those `li` elements that you need to extend:

```html
<li class="nav-item">
<a class="nav-link" href="/about/">About</a>
</li>
```

That's all - after app reload (`docker-compose restart`) you should see new page.

## How to add new blog post

Adding posts are done manually in the code - so it is for old pricks like me (no UI here).

So you need to create markdown file in `content/` directory in the right 
`date` location, so `content/2017/07/04/some-slug.md`.

After you create the content file, go and open `posts.json` file and add there meta 
information about post you just created.

Later on you can update the markdown file with the content. Why markdown? Cause I believe it is 
the fastest way of creating documents that actually looks nice. Of course we can use html WYSIWYG
editors to create nice looking blog posts - but I didn't really like it - well probably just me.

## Others

I am using free [Clean Blog template](https://startbootstrap.com/themes/clean-blog/) Great work guys!

Somebody asked me: Why no markdown -> html conversion and server statics instead?
Well - IT IS NO FUN. 

You can always write me a note here: [sebastian@trurl.it](mailto:sebastian@trurl.it)