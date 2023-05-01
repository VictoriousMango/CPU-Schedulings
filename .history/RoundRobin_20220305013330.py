from prettytable import PrettyTable as PT
# Round Robin Scheduling Algorithm
 
# Function to find the waiting time for all processes
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
    total_wt = 0
    total_tat = 0
    for i in range(n):
 
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        l1.append(str(wt[i]))
        l2.append(str(tat[i]))
        mytable.add_row([str(i + 1),str(bt[i]),str(wt[i]),str(tat[i])])
        #print(" ", i + 1, "\t\t", bt[i],
        #      "\t\t", wt[i], "\t\t", tat[i])
 
    print("\nAverage waiting time = %.5f "%(total_wt /n) )
    print("Average turn around time = %.5f "% (total_tat / n))
     
# Driver code
if __name__ =="__main__":
     
    # Process id's
    proc = [i for i in range(6)]
    n = len(proc)
 
    # Burst time of all processes
    fibonacci_series = lambda x: x if x <= 1 else fibonacci_series(x-1) + fibonacci_series(x-2)  
    burst_time = [fibonacci_series(i) for i in range(2, 2 + n)]
 
    # Time quantum
    quantum = 2;

    mytable = PT(["Processes","Burst Time","Waiting Time","Turn Around Time"])
    l1= burst_time
    l2=[]
    l3=[]

    findavgTime(proc, n, burst_time, quantum)
    print(mytable)