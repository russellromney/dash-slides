# dash-slides

Make easy interactive presentation slides in Python with Dash. 

Example app at https://dash-slides.fly.dev/

This is a Dash app with built in slide navigation, logo, web title, etc. Just run `python3 app.py` in a terminal to see it work!

## To use:

```shell
git clone https://github.com/russellromney/dash-slides
cd dash-slides
```

Using pip virtualenv:

```shell
virtualenv env
source env/bin/activate
pip install -r requirements.txt
python3 app.py
```

Or, my preferred way, using `poetry`:

```shell
poetry shell
poetry install
python3 app.py
```

![example gif](https://raw.githubusercontent.com/russellromney/dash-slides/master/example/assets/example_gif.gif)


**Making your own presentation**

1. Download, clone, or fork `dash-slides/`.
1. Delete the example slides and add your own slides (individual Dash apps) in `slides/` as files with content and associated callbacks, with a filename like `<slide_name>.py`.
   - Slide names must be valid Python variable names e.g. `example.py` or `_intro5.py` but not `my great slide.py` or `5 people.py`.
   - Each slide's layout is stored in a variable named `content`, e.g. `content = html.Div...` (similar to multipage Dash app where each page has a `layout = html.Div...`
   - Every slide needs `from app import app` at the beginning
3. Configure the presentation in  `presentation.py`:
   - List your slides' names in order (without the `.py`) in `slide_order`
   - e.g. `slide_order = ['intro','template','last_slide','end']`
2. Store custom functions, utilities, objects, etc. in `custom_utilities/` or however else you'd like.
4. `pip install dash dash-bootstrap-components`
   - the navigation depends on it

Then run it like a normal Dash app with `python app.py` or using Gunicorn or whatever else you'd normally use with Dash or Flask.

For the curious, there's a Dockerfile included to run this with `gunicorn` workers.

How this would look:
```
# files structure
/dash-slides
   /assets
   /slides
      intro.py
      body1.py
      body2.py
      conclusion.py
   index.py
   app.py
   presentation.py

# in /slides/presentation.py
slide_order = [
    'intro',
    'body1',
    'body2',
    'conclusion'
]
...
```

---

## More custom stuff

**Logo:** Replace `assets/logo.png` with your own file named `logo.png` for your logo to appear on all slides.

**Favicon:** Like a normal Dash app, replace `assets/favicon.ico` with your own favicon for an even more custom experience.

**Title:** Give your presentation a title by changing `presentation_title`.

**Custom navigation text:** Replace `prev_text` and `next_text` values with new words to have any navigation text you want.



---

## Free deployment on [fly.io](https://fly.io)

You can deploy to free to https://fly.io with automatic HTTPS and a URL!

I've included a `Dockerfile` for you - just install flyctl (https://fly.io/docs/hands-on/install-flyctl/) and create a free account, then do:

```shell
fly launch
```

It will prompt you for an app name and a region and create a `fly.toml` file; your app will then be available at https://app-name.fly.dev.

If you don't deploy immediately, or to redeploy after changes do:

```shell
fly deploy
```

again.
---

Made with :heart: by Russell Romney in Madison, WI and NYC.

> Shoutout to Tom Begley's excellent `dash-bootstrap-components` package, used here to make prettify navigation.
