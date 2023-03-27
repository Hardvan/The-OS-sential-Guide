# cd to the folder where the app.py file is located
# run the command: python app.py

from flask import Flask, render_template, request
import scheduling_algos

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

        no_processes = int(request.form.get('num_processes'))
        print(no_processes)

        return render_template('cpu.html', no_processes=no_processes)

    return render_template('cpu.html')


@app.route('/cpu_result', methods=['GET', 'POST'])
def cpu_result():

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
        FCFS_result = scheduling_algos.fcfs(processes)

        # Run SJF algorithm
        SJF_result = scheduling_algos.sjf(processes)

        # Run Priority algorithm
        Priority_result = scheduling_algos.priority(processes)

        return render_template('cpu_result.html',
                               FCFS_result=FCFS_result,
                               SJF_result=SJF_result,
                               Priority_result=Priority_result)


if __name__ == "__main__":
    app.run(debug=True)
