# dash-slides

Make truly interactive slides in Python with Plotly Dash.

![logo](https://raw.githubusercontent.com/russellromney/dash-slides/master/dash-slides/assets/logo.png)

---

This is a Dash app with built in slide navigation, logo, web title, etc. An example is in `example/` 

## To use:

1. Download, clone, or fork `dash-slides/`.
1. Put slides (individual Dash apps) in `slides/` as `<slide_name>.py` files with callbacks and content.
   - Slide names must be valid Python variable names.
   - The index function expects the slide's content to be named like `content = html.Div...` (similar to multipage Dash app where each page has a `layout = html.Div...`
   - Do not remove `from app import app` from any slide.
3. In `presentation.py`:
   - List your slides' names in order (without the `.py`) in `slide_order`
2. Store custom functions, utilities, objects, etc. in `custom_utilities/` or however else.

Then run it like a normal Dash app with `python index.py` or using Gunicorn or whatever else you'd like. 

![gif](https://media.giphy.com/media/YPt6omcsn3Q5iabl9V/giphy.gif)

---

## More custom stuff

**Logo:** Replace `assets/logo.png` with your own file named `logo.<format>` for your logo to appear on all slides.

**Favicon:** Like a normal Dash app, replace `assets/favicon.ico` with your own favicon for an even more custom experience.

**Title:** Give your presentation a title by changing `presentation_title`.

**Custom navigation text:** Replace `prev_text` and `next_text` with new words to have any navigation text you want.


---

Made with :heart: by Russell Romney in Madison, WI.
