# Priority Scheduling
 
# Function to find the waiting time for all processes
def findWaitingTime(processes, n, waiting_time):
    waiting_time[0] = 0
    for i in range(1, n):
        waiting_time[i] = processes[i - 1][1] + waiting_time[i - 1]
 
# Function to calculate turn around time
def findTurnAroundTime(processes, n, waiting_time, tat):
    for i in range(n):
        tat[i] = processes[i][1] + waiting_time[i]
 
# Function to calculate average waiting and turn-around times.
def findavgTime(processes, n):
    waiting_time = [0] * n
    tat = [0] * n
    findWaitingTime(processes, n, waiting_time)
    findTurnAroundTime(processes, n, waiting_time, tat)
    print("\nProcesses    Burst Time    Waiting",
          "Time    Turn-Around Time")
    total_waiting_time = 0
    total_tat = 0
    for i in range(n):
 
        total_waiting_time = total_waiting_time + waiting_time[i]
        total_tat = total_tat + tat[i]
        print(" ", processes[i][0], "\t\t",
                   processes[i][1], "\t\t",
                   waiting_time[i], "\t\t", tat[i])
 
    print("\nAverage waiting time = %.5f "%(total_waiting_time /n))
    print("Average turn around time = ", total_tat / n)
 
def priorityScheduling(proc, n):
     
    # Sort processes by priority
    proc = sorted(proc, key = lambda proc:proc[2],
                                  reverse = True);
 
    print("Order in which processes gets executed")
    for i in proc:
        print(i[0], end = " ")
    findavgTime(proc, n)
     
# Driver code
if __name__ =="__main__":
     
    # Process id's
    proc = [[1, 3, 19],
            [2, 11, 16],
            [3, 1, 14],
            [4, 13, 0],
            [5, 6, 5],
            [6, 4, 23],
            [7, 17, 8],
            [8, 2, 6]]
    n = 8
    priorityScheduling(proc, n)