# cd to the folder where the app.py file is located
# run the command: python app.py

from flask import Flask, render_template, request
import scheduling_algos

app = Flask(__name__)

no_processes = 0
time_quantum = 0


@app.route('/')
def index():
    """Home Page

    Returns:
        [html]: [Home Page]
    """

    return render_template("index.html")


@app.route('/cpu', methods=['GET', 'POST'])
def cpu():
    """CPU Scheduling Page

    Returns:
        [html]: [CPU Scheduling Page]
    """

    if request.method == 'POST':

        global no_processes
        global time_quantum
        no_processes = int(request.form.get('num_processes'))
        time_quantum = int(request.form.get('time_quantum'))
        print(no_processes, time_quantum)

        return render_template('cpu.html', no_processes=no_processes)

    return render_template('cpu.html', no_processes=no_processes)


@app.route('/cpu_result', methods=['GET', 'POST'])
def cpu_result():

    if request.method == 'POST':

        # Converting form data to a list of tuples
        processes = []
        for i in range(1, no_processes+1):
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

        # Run Round Robin algorithm
        global time_quantum
        RR_result = scheduling_algos.round_robin(processes, time_quantum)

        return render_template('cpu_result.html',
                               FCFS_result=FCFS_result,
                               SJF_result=SJF_result,
                               Priority_result=Priority_result,
                               RR_result=RR_result)


@app.route('/prosync')
def prosync():
    """Prosync Page

    Returns:
        [html]: [Prosync Page]
    """

    return render_template("prosync.html")


@app.route('/classicprosync')
def classicprosync():
    """Classic Prosync Page

    Returns:
        [html]: [Classic Prosync Page]
    """

    return render_template("classicprosync.html")


@app.route('/thread')
def thread():
    """Thread Scheduling Page

    Returns:
        [html]: [Thread Scheduling Page]
    """

    return render_template("thread.html")


if __name__ == "__main__":
    app.run(debug=True)
