# This is sample post

## lets write your own

# You can add whatever markup that markdown supports.

## lists

this:

```markdown
* this is a list
* an here is a second element 
```

becomes this:

* this is a list
* an here is a second element 

## tables

this:

```markdown
| column A | column B | Column C |
| --- | --- | --- |
| 0 | 1 | 2 |
| 3 | 4 | 5 |
| 6 | 7 | 8 |

```

becomes this:

| column A | column B | Column C |
| --- | --- | --- |
| 0 | 1 | 2 |
| 3 | 4 | 5 |
| 6 | 7 | 8 |

## links

this:
```markdown
[this is a link](https://example.org)
```

becomes this:

[this is a link](https://example.org)

## images

this:
```markdown
![this is alt image](https://upload.wikimedia.org/wikipedia/en/a/a9/Example.jpg)
```

becomes this:

![this is alt image](https://upload.wikimedia.org/wikipedia/en/a/a9/Example.jpg)

### images that you own

Put a file under `blog/content/resources`, eg. `example.png`

Then you can refer to it as `/resources/example.png`, so:

```markdown
![Some alt text](/resources/sample-post/sample-image.jpg)
```

will produce:

![Some alt text](/resources/sample-post/sample-image.jpg)

## code blocks

As I am running technical block - the syntax highlighting is working using `higlight.js`.

so this:
````markdown
```python

class SomeClass:

    def __init__(self, param):
        self.param = param
        
    def hello(self):
        print(f"Hello, I am {self.__class__.__name__}:{self.param}")
```
````

will become this:

```python

class SomeClass:

    def __init__(self, param):
        self.param = param
        
    def hello(self):
        print(f"Hello, I am {self.__class__.__name__}:{self.param}")

```

## text stuff

this:

```markdown
This is simple paragraph, it should be indented - for me it looks a bit nicer, but you can 
always change your css styles (you actually own them).


**bold text**

*italic text*

`code-text` - it will be nicely formatted as pink-like monospace text

# header1
## header2
### header3
#### header4
##### header5
```

becomes this:

This is simple paragraph, it should be indented - for me it looks a bit nicer, but you can 
always change your css styles (you actually own them).

**bold text**

*italic text*

`code-text` - it will be nicely formatted as pink-like monospace text

# header1
## header2
### header3
#### header4
##### header5