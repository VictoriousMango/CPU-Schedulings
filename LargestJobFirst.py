# Largest Job First Scheduling Algorithm
p = [] 
for i in range(4): 
    p.append([0, 0, 0, 0, 0, 0, 0]) 
totaltime = 0
prefinaltotal = 0
def findlargest(at): 
    max = 0
    for i in range(4): 
        if (p[i][1] <= at): 
            if (p[i][2] > p[max][2]) : 
                max = i 
    return max

# function to find the completion time of each process 
def findCT(totaltime): 
    index = 0
    flag = 0
    i = p[0][1] 
    while (1): 
        if (i <= 4): 
            index = findlargest(i) 
        else: 
            index = findlargest(4) 
        p[index][2] -= 1
        totaltime += 1
        i += 1
        if (p[index][2] == 0): 
                p[index][6] = totaltime 
        if (totaltime == prefinaltotal): 
            break

# Driver code 
if __name__ =="__main__": 
    for i in range(4): 
        p[i][0] = i + 1

    for i in range(4):
        p[i][1] = i + 1

    for i in range(4): 
        p[i][2] = 2 * (i + 1) 
        p[i][3] = p[i][2] 
        prefinaltotal += p[i][2]  
    p = sorted(p, key = lambda p:p[1]) 
    totaltime += p[0][1] 
    prefinaltotal += p[0][1] 
    findCT(totaltime) 
    totalWT = 0
    totalTAT = 0
    for i in range(4): 
        p[i][5] = p[i][6]- p[i][1] 
        p[i][4] = p[i][5] - p[i][3] 
        totalWT += p[i][4] 
        totalTAT += p[i][5] 

    print("Process \t Burst Time \t Waiting Time \t Turn Around Time " )

    for i in range(4): 
        print(p[i][0], "\t", p[i][3], "\t", end = " ") 
        print(p[i][4], "\t", p[i][5]) 
    print() 
    print("Total waiting time = ", totalWT)  
    print("Average turn around time = ", totalTAT / 4.0) 
