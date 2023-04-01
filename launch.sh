# install deps
pip install --upgrade pip
pip install -r requirements.txt

# launch app
gunicorn -w 4 'app.main:app'