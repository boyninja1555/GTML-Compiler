# GTML Documentation

Getting bored of HTML? GTML offers a different way of coding websites that is more similar to other languages and makes words make more sense like for example, "href", is now, "url", and, "src", is now, "url". I also made different tags live up their meaning like the, "`<a>`", tag is now, "{hyperlink}", but the rest of the syntax is like HTML with this being a tag:

````gtml
{hyperlink url="https://www.example.com"}This is a hyperlink!{END:hyperlink}

````

Yup, it is very similar to HTML but also makes more sense. here is some starter code:

```gtml
{settings}
    {lang lang="en-us"}{END:lang}
    {page_title}GTML Test{END:page_title}
    {page_icon url="/favicon.png"}{END:page_icon}
{END:settings}
{main}
    {heading}Hello world!{END:heading}
    {text}This is an example of GTML (Gmoney Text Markup Language){END:text}
    {hyperlink url="https://www.example.com"}This is a link{END:hyperlink}
    {script url="/js/script0.js"}{END:script}
{END:main}

```

I will give you the current wiki or translator for all the tags I have implimented.

## GTML Tags Wiki & Translator

```gtml
{settings}
```

Translates to:

```html
<html>
```

The end tag is:

```gtml
{END:settings}
```

---

```gtml
{lang lang="your_language_here"}
```

Translates to:

```html
<html lang="en"> // The HTML part of the tag is not part of what the lang tag does, the lang tag just adds the lang attribute to the HTML tag
```

The end tag is:

```gtml
{END:lang}
```
