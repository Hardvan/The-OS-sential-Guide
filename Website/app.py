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

        # Converting form data to a list of tuples
        processes = []
        for i in range(1, 5):
            pid = f'P{i}'
            arrival_time = int(request.form.get(f'arrival_time_{i}'))
            burst_time = int(request.form.get(f'burst_time_{i}'))
            priority = int(request.form.get(f'priority_{i}'))
            processes.append((pid, arrival_time, burst_time, priority))

        print(processes)  # Testing

        # ? FCFS Algorithm
        processes.sort(key=lambda x: x[1])  # Sort by arrival time
        completion_times = []
        waiting_times = []
        turnaround_times = []
        current_time = 0
        for process in processes:
            pid, arrival_time, burst_time, priority = process

            current_time = max(current_time, arrival_time)

            completion_time = current_time + burst_time
            waiting_time = current_time - arrival_time
            turnaround_time = waiting_time + burst_time

            completion_times.append(completion_time)
            waiting_times.append(waiting_time)
            turnaround_times.append(turnaround_time)

            current_time = completion_time

        average_waiting_time = sum(waiting_times) / len(waiting_times)
        average_turnaround_time = sum(turnaround_times) / len(turnaround_times)

        FCFS_result = {}
        FCFS_result['processes'] = processes
        FCFS_result['completion_times'] = completion_times
        FCFS_result['waiting_times'] = waiting_times
        FCFS_result['turnaround_times'] = turnaround_times
        FCFS_result['average_waiting_time'] = average_waiting_time
        FCFS_result['average_turnaround_time'] = average_turnaround_time

        return render_template("cpu_result.html", FCFS_result=FCFS_result)

    return render_template("cpu.html")


if __name__ == "__main__":
    app.run(debug=True)
