import os
from flask import Flask

app = Flask(__name__, static_folder="static")
app.root_path = app.root_path.replace(f'{os.sep}support','')
app.config.from_pyfile(f'{app.root_path}{os.sep}flask_app_config.cfg')