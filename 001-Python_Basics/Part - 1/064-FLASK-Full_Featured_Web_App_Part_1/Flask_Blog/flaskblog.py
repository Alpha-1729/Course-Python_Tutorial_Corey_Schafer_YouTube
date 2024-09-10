from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return "<h1>Hello World</h1>"


@app.route("/about")
def about():
    return "<h1>About Page</h1>"


# By the below line, you can directly run this web server.
if __name__ == "__main__":
    app.run(debug=True)
