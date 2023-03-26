# cd to the folder where the app.py file is located
# run the command: python app.py

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    """Home Page

    Returns:
        [html]: [Home Page]
    """

    return render_template("home.html")


@app.route('/cpu', methods=['GET', 'POST'])
def cpu():
    """CPU Scheduling Page

    Returns:
        [html]: [CPU Scheduling Page]
    """

    if request.method == 'POST':
        # Get form data
        data = []
        for i in range(1, 5):
            arrival_time = request.form.get(f'arrival_time_{i}')
            burst_time = request.form.get(f'burst_time_{i}')
            priority = request.form.get(f'priority_{i}')
            data.append({'arrival_time': arrival_time,
                        'burst_time': burst_time, 'priority': priority})
        # Do something with the data
        print(data)

        # TODO: Redirect to cpu.html with the data
        return "Form submitted successfully!"

    return render_template("cpu.html")


if __name__ == "__main__":
    app.run(debug=True)
