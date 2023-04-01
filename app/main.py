import dotenv
from flask import Flask
from flask import render_template
from flask_cors import CORS
import os

# Load env
dotenv.load_dotenv()

# App config
SECRET_KEY = os.environ.get('SECRET_KEY')
ALLOWED_CORS = os.environ.get('ALLOWED_CORS').split(';')

# Init app
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": ALLOWED_CORS}})


# Game route
@app.route("/")
def render_game():
    return render_template('index.html')