# cd to the folder where the app.py file is located
# run the command: python app.py

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("basic.html")


if __name__ == "__main__":
    app.run(debug=True)
