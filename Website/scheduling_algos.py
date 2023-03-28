import copy


def fcfs(processes):
    """First Come First Serve (FCFS) CPU Scheduling Algorithm

    Args:
        processes (list): List of processes (tuples)

    Returns:
        result (dict): Dictionary containing the following:
        - processes (list): List of processes (tuples)
        - start_times (list): List of start times (int)
        - completion_times (list): List of completion times (int)
        - waiting_times (list): List of waiting times (int)
        - turnaround_times (list): List of turnaround times (int)
        - average_waiting_time (float): Average waiting time (float)
        - average_turnaround_time (float): Average turnaround time (float)
    """

    processes = copy.deepcopy(processes)

    processes.sort(key=lambda x: x[1])  # Sort by arrival time
    start_times = []
    burst_times = [process[2] for process in processes]
    completion_times = []
    waiting_times = []
    turnaround_times = []
    current_time = 0

    for process in processes:
        pid, arrival_time, burst_time, priority = process

        current_time = max(current_time, arrival_time)
        start_time = current_time  # Store the start time

        completion_time = current_time + burst_time
        waiting_time = current_time - arrival_time
        turnaround_time = waiting_time + burst_time

        start_times.append(start_time)
        completion_times.append(completion_time)
        waiting_times.append(waiting_time)
        turnaround_times.append(turnaround_time)

        current_time = completion_time

    average_waiting_time = sum(waiting_times) / len(waiting_times)
    average_turnaround_time = sum(turnaround_times) / len(turnaround_times)

    result = {}
    result['processes'] = processes
    result['start_times'] = start_times
    result['burst_times'] = burst_times
    result['completion_times'] = completion_times
    result['waiting_times'] = waiting_times
    result['turnaround_times'] = turnaround_times
    result['average_waiting_time'] = average_waiting_time
    result['average_turnaround_time'] = average_turnaround_time

    return result


def sjf(processes):
    """Shortest Job First (SJF) CPU Scheduling Algorithm

    Args:
        processes (list): List of processes (tuples)

    Returns:
        result (dict): Dictionary containing the following:
        - processes (list): List of processes (tuples)
        - completion_times (list): List of completion times (int)
        - waiting_times (list): List of waiting times (int)
        - turnaround_times (list): List of turnaround times (int)
        - average_waiting_time (float): Average waiting time (float)
        - average_turnaround_time (float): Average turnaround time (float)
    """

    processes = copy.deepcopy(processes)

    processes_sorted = sorted(
        processes, key=lambda x: x[2])  # Sort by burst time
    completion_times = []
    waiting_times = []
    turnaround_times = []
    current_time = 0

    while processes_sorted:
        # Select the process with the shortest burst time
        next_process = processes_sorted.pop(0)
        pid, arrival_time, burst_time, priority = next_process

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

    result = {}
    result['processes'] = processes
    result['completion_times'] = completion_times
    result['waiting_times'] = waiting_times
    result['turnaround_times'] = turnaround_times
    result['average_waiting_time'] = average_waiting_time
    result['average_turnaround_time'] = average_turnaround_time

    return result


def priority(processes):
    """Priority Scheduling CPU Scheduling Algorithm

    Args:
        processes (list): List of processes (tuples) with (pid, arrival_time, burst_time, priority)

    Returns:
        result (dict): Dictionary containing the following:
        - processes (list): List of processes (tuples)
        - completion_times (list): List of completion times (int)
        - waiting_times (list): List of waiting times (int)
        - turnaround_times (list): List of turnaround times (int)
        - average_waiting_time (float): Average waiting time (float)
        - average_turnaround_time (float): Average turnaround time (float)
    """
    processes = copy.deepcopy(processes)

    # Sort the processes by priority in ascending order
    processes.sort(key=lambda x: x[3])

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

    result = {}
    result['processes'] = processes
    result['completion_times'] = completion_times
    result['waiting_times'] = waiting_times
    result['turnaround_times'] = turnaround_times
    result['average_waiting_time'] = average_waiting_time
    result['average_turnaround_time'] = average_turnaround_time

    return result


def round_robin(processes, quantum):
    """Round Robin CPU Scheduling Algorithm

    Args:
        processes (list): List of processes (tuples)
        quantum (int): Time quantum for each process

    Returns:
        result (dict): Dictionary containing the following:
        - processes (list): List of processes (tuples)
        - completion_times (list): List of completion times (int)
        - waiting_times (list): List of waiting times (int)
        - turnaround_times (list): List of turnaround times (int)
        - average_waiting_time (float): Average waiting time (float)
        - average_turnaround_time (float): Average turnaround time (float)
    """

    processes = copy.deepcopy(processes)

    completion_times = [0] * len(processes)
    waiting_times = [0] * len(processes)
    turnaround_times = [0] * len(processes)
    remaining_times = [burst_time for pid,
                       arrival_time, burst_time, priority in processes]
    current_time = 0
    quantum_left = 0

    while True:
        done = True
        for i, process in enumerate(processes):
            pid, arrival_time, burst_time, priority = process
            if remaining_times[i] > 0:
                done = False
                if remaining_times[i] <= quantum:
                    quantum_left = remaining_times[i]
                else:
                    quantum_left = quantum
                current_time += quantum_left
                remaining_times[i] -= quantum_left
                if remaining_times[i] == 0:
                    completion_times[i] = current_time
                    waiting_times[i] = completion_times[i] - \
                        arrival_time - burst_time
                    turnaround_times[i] = completion_times[i] - arrival_time
        if done:
            break

    average_waiting_time = sum(waiting_times) / len(waiting_times)
    average_turnaround_time = sum(turnaround_times) / len(turnaround_times)

    result = {}
    result['processes'] = processes
    result['completion_times'] = completion_times
    result['waiting_times'] = waiting_times
    result['turnaround_times'] = turnaround_times
    result['average_waiting_time'] = average_waiting_time
    result['average_turnaround_time'] = average_turnaround_time
    result["quantum"] = quantum

    return result
