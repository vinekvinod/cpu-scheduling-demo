# rr.py - Round Robin CPU Scheduling

def round_robin(processes, burst_time, arrival_time, quantum):
    n = len(processes)
    remaining_bt = burst_time[:]
    t = 0
    waiting_time = [0] * n
    turnaround_time = [0] * n
    gantt_chart = []

    while True:
        done = True
        for i in range(n):
            if remaining_bt[i] > 0 and arrival_time[i] <= t:
                done = False
                gantt_chart.append((processes[i], t, min(t + quantum, t + remaining_bt[i])))
                
                if remaining_bt[i] > quantum:
                    t += quantum
                    remaining_bt[i] -= quantum
                else:
                    t += remaining_bt[i]
                    waiting_time[i] = t - burst_time[i] - arrival_time[i]
                    turnaround_time[i] = t - arrival_time[i]
                    remaining_bt[i] = 0
        if done:
            break

    avg_wt = sum(waiting_time) / n
    avg_tat = sum(turnaround_time) / n

    print("Process\tBT\tAT\tWT\tTAT")
    for i in range(n):
        print(f"{processes[i]}\t{burst_time[i]}\t{arrival_time[i]}\t{waiting_time[i]}\t{turnaround_time[i]}")

    print("\nAverage Waiting Time:", round(avg_wt, 2))
    print("Average Turnaround Time:", round(avg_tat, 2))

    print("\nGantt Chart:")
    for g in gantt_chart:
        print(f"| {g[0]} ({g[1]}→{g[2]}) ", end="")
    print("|")


# Example usage
processes = ["P1", "P2", "P3"]
burst_time = [10, 5, 8]
arrival_time = [0, 1, 2]
quantum = 3

round_robin(processes, burst_time, arrival_time, quantum)
