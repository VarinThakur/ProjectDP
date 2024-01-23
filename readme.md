Steps to run the project -

1. Ensure you're running python 3.11
    `python --version`

2. Install virtualenv to create a virtual environment
    `pip install virtualenv`

3. Create a virtual environment
    `virtualenv env`

4. Activate the virtual environment

    On Windows
    `\env\Scripts\activate`

    On Linux
    `env/Scripts/activate.sh`

5. Install the required dependencies
    `pip install -r requirements.txt`

6. Go to the ProjectDP directory

    `cd ProjectDP`

7. Run the App (/plotter endpoint for finding the plot)

    `python manage.py runserver`


Refered links for making the project -

- https://github.com/holoviz/panel/issues/865
- https://panel.holoviz.org/how_to/integrations/Django.html
- https://panel.holoviz.org/getting_started/build_app.html
- https://discourse.holoviz.org/t/unable-to-load-autoload-js/5573
- https://github.com/holoviz/panel/issues/4876
- https://github.com/bokeh/bokeh-django/blob/main/README.md
- https://discourse.holoviz.org/t/unable-to-add-panel-to-django/2417
- https://github.com/holoviz/panel/issues/1233
- https://stackoverflow.com/questions/74280959/attributeerror-unexpected-attribute-plot-width-to-figure-similar-attributes

