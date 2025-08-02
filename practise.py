def sjf(processes,bt):
    n= len(processes)
    zipped= sorted(zip(bt,processes))
    bt, processes= zip(*zipped)
    wt= [0]*n
    TA= [0]*n
    for i in range(1,n):
        wt[i]= wt[i-1]+ bt[i-1]
    for i in range(n):
        TA[i]= wt[i] + bt[i]

    print("sjf schedule:")
    for i in range(n):
        print(f"p{processes [i]}: waiting={wt[i]}: turnaround={TA[i]}:")

processes = [1,2,3]
bt = [5,2,8]
sjf(processes,bt)             