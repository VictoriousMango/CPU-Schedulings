#Python3 program for implementation of
# RR scheduling
 
# Function to find the waiting time
# for all processes
def findWaitingTime(processes, n, bt,
                         wt, quantum):
    rem_bt = [0] * n
    for i in range(n):
        rem_bt[i] = bt[i]
    t = 0
    while(1):
        done = True
        for i in range(n):
            if (rem_bt[i] > 0) :
                done = False
                 
                if (rem_bt[i] > quantum) :
                    t += quantum
                    rem_bt[i] -= quantum
                else:
                    t = t + rem_bt[i]
                    wt[i] = t - bt[i]
                    rem_bt[i] = 0
        if (done == True):
            break
             
# Function to calculate turn around time
def findTurnAroundTime(processes, n, bt, wt, tat):
    for i in range(n):
        tat[i] = bt[i] + wt[i]
 
 
# Function to calculate average waiting and turn-around times.
def findavgTime(processes, n, bt, quantum):
    wt = [0] * n
    tat = [0] * n
 
    # Function to find waiting time of all processes
    findWaitingTime(processes, n, bt,
                         wt, quantum)
 
    # Function to find turn around time for all processes
    findTurnAroundTime(processes, n, bt,
                                wt, tat)
 
    # Display processes along with all details
    print("Processes    Burst Time     Waiting",
                     "Time    Turn-Around Time")
    total_wt = 0
    total_tat = 0
    for i in range(n):
 
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        print(" ", i + 1, "\t\t", bt[i],
              "\t\t", wt[i], "\t\t", tat[i])
 
    print("\nAverage waiting time = %.5f "%(total_wt /n) )
    print("Average turn around time = %.5f "% (total_tat / n))
     
# Driver code
if __name__ =="__main__":
     
    # Process id's
    proc = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    n = len(proc)
 
    # Burst time of all processes
    fibs = [lambda x, _: x + [x[-2] + x[-1]], [0] * (n-2), [0, 1]]
    burst_time = [fibs]
 
    # Time quantum
    quantum = 2;
    findavgTime(proc, n, burst_time, quantum)