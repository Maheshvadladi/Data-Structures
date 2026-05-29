# activity selection
'''def activityselection(start, finish):
    n = len(start)
    act = []
    for i in range(n):
        act.append((finish[i], start[i]))
    act.sort()
    print("Selected activites: ")
    last_finish = act[0][0]
    print(f"Start: {act[0][1]}, End: {act[0][0]}")
    for i in range(1,n):
        current_start = act[i][1]
        current_finish = act[i][0]
        if current_start >= last_finish:
            print(f"start: {current_start}, End: {current_start}")
            last_finish= current_start
n = int(input("Enter number of activites: "))
start = []
finish = []
for i in range(n):
    s = int(input(f"Enter start time activites{i+1}: "))
    f = int(input(F"Enter end time activity{i+1}: "))
    start.append(s)
    finish.append(f)
activityselection(start, finish)'''