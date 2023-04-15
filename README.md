# Bitok Loader Game
Mini game for bitok loader on Flask

## Launch
To launch app use launch.sh script, it needs to install dependencies and start wsgi server. 
By default, it using 4 workers of gunicorn, but you can use anything you need, just edit 6th row of launch.sh and update requirements.
Learn more about [Flask deployment](https://flask.palletsprojects.com/en/2.2.x/deploying/)

## Settings
All settings stored in .env. This app provides two settings:
1. ### ***Secret key***
    It's a secret key that will be used for securely signing the session cookie and can be used for any other security related needs.
    It need to be a random bytes or str. [More about secret key](https://flask.palletsprojects.com/en/2.2.x/tutorial/deploy/?highlight=secret%20key)
2. ### ***Allowed CORS***
    ***CORS*** is a Cross Origin Resource Sharing, it's needs to share static files or another data across web services.
    you need to provide your domains and ip's where you want to use data of this application as string separated by ";".
    [More about CORS](https://flask-cors.readthedocs.io/en/latest/)
    > Defaults to "*"

## Technologies
### List of technologies used in this app:
+ ***Flask***
+ ***Gunicorn***
+ ***FlaskCORS***

## Integration
To integrate this app on your site you need to host this app and 
add ***iframe*** tag to your site with url of your hosted app as ***iframe src*** and
this css styles of this ***iframe***:
```
position:fixed;
top:0;
left:0;
bottom:0;
right:0;
width:100%;
height:100%;
border:none;
margin:0;
padding:0;
overflow:hidden;
z-index:999999;
```
## Example
To test this app you can use ***venv*** from root of this page, launch app and open ***iframe_example.html*** 

## Dependencies
All dependencies stored in requirements.txt, you can find it in a root directory