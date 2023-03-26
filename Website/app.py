# cd to the folder where the app.py file is located
# run the command: python app.py

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """Home Page

    Returns:
        [html]: [Home Page]
    """

    return render_template("home.html")


@app.route('/cpu')
def cpu():
    """CPU Scheduling Page

    Returns:
        [html]: [CPU Scheduling Page]
    """
    return render_template("cpu.html")


if __name__ == "__main__":
    app.run(debug=True)
