# Song Lyrics Application

Lyrics App is a django application that takes artist and song inputs, and displays the lyrics to the matching song. It also displays random lyrics and the most searched songs if requested.

## Installation

This project runs on Django 2.1.7

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the following packages.

```bash
pip install Django==2.1.7
pip install beautifulsoup4
pip install requests
pip install lxml
```

## Usage

```python

python manage.py migrate
pythin manage.py makemigrations songs_app
python manage.py migrate
python manage.py runserver
```

Copy IP address displayed in console into a web browser to run the application.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
