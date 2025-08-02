# FCFS Scheduling
def fcfs(processes, burst_time):
    n = len(processes)
    wt = [0] * n
    TA = [0] * n

    for i in range(1, n):
        wt[i] = wt[i - 1] + burst_time[i - 1]
    
    for i in range(n):
        TA[i] = wt[i] + burst_time[i]

    print("FCFS Schedule:")
    for i in range(n):
        print(f"P{processes[i]}: Waiting={wt[i]}, Turnaround={TA[i]}")


#test
processes = [1, 2, 3]
burst_time = [5, 2, 8]
fcfs(processes, burst_time)