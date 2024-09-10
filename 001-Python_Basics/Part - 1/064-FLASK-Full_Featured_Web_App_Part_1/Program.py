#!/usr/bin/python3
# Full Featured Web App Part 1

"""
>>>> In this video, we are using flask framework in python.
        Flask is an excellent micro framework.
>>>> Install Flask.
        pipenv install Flask
>>>> Flask Documentation.
        Reference Link: https://flask.palletsprojects.com/en/3.0.x/quickstart/#a-minimal-application
>>>> Routes
        Route are what we type into our browser to get different pages.
>>>> Running a flask application.
        Method 1
            Go to the Flask application folder.
            Open in terminal.
            set and environment variable for flask app.
                For Linux
                    export FLASK_APP=flaskblog.py
                    export FLASK_DEBUG=1
                For Windows
                    set FLASK_APP=flaskblog.py
                    set FLASK_DEBUG=1
            flask run
        Method 2:
            Add the below code at the end of the flask application. 
            if __name__ == "__main__":
                app.run(debug=True)



        Visit http://127.0.0.1:5000 OR http://localhost:5000 to view the web server.
>>>> Restart the server if you change the code.
        Run app in DEBUG mode to see live code changes without restarting server.
>>>> 
>>>> 
>>>> 
"""
