# SIMPLE BLOG PLATFORM

## Why?

Literally - because I can.

I know that there are tons of solutions for handling blog, but I wanted to have mine :) 

## Benefits?

* No database
* No nothing - only this docker image

## How use it?

    docker-compose up -d

Go to http://localhost:8031

You should see samples posts.

Adding posts are done manually in the code - so it is for old pricks like me (no UI here).

So you need to create markdown file in `content/` directory.

After you create the content file, go and open `posts.json` file and add there meta 
information about post you just created.

```json
    {
      "title":  "This is sample post.",
      "href_name": "sample-post.html",
      "date": "28-06-2019 15:43",
      "author": "John Watch",
      "intro": "And this is sample post intro"
    }
```

Posts are list there - so extend the list not replace.

Btw. I have no pagination yet - but who cares; only few of blogs has more than 100 posts.
Usually people lost enthusiasm lot earlier.

After changes - you need to rebuild image and restart application.
It can be very nicely incorporated into CI/CD - this what I am doing.


## To change bg image

Change the `static/img/home-bg.jpg` to whatever you like.
Same story with `favicon.ico` -> pyt there whatever you like.
To add image to your posts - add them under `static/img/posts` (you can organize this on your own);

There's an example of how to do it in `sample-post.md`.
