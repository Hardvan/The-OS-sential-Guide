# cd to the folder where the app.py file is located
# run the command: python app.py

from flask import Flask, render_template, request
from scheduling_algos import fcfs, sjf

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

        # Converting form data to a list of tuples
        processes = []
        for i in range(1, 5):
            pid = f'P{i}'
            arrival_time = int(request.form.get(f'arrival_time_{i}'))
            burst_time = int(request.form.get(f'burst_time_{i}'))
            priority = int(request.form.get(f'priority_{i}'))
            processes.append((pid, arrival_time, burst_time, priority))

        # Run FCFS algorithm
        FCFS_result = fcfs(processes)

        # Run SJF algorithm
        SJF_result = sjf(processes)

        return render_template('cpu_result.html', FCFS_result=FCFS_result, SJF_result=SJF_result)

    return render_template('cpu.html')


if __name__ == "__main__":
    app.run(debug=True)
