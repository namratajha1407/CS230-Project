import matplotlib.pyplot as plt

ipc = []
llc_miss_rate = []
l1d_miss_rate = []
l1i_miss_rate = []
l2_miss_rate = []
trace = ["sssp-14", "bfs-3", "cc-6"]
rep = ["fifo", "lfu", "lru", "random", "drrip"]
index= [0,1,2,3,4]
for i in trace:
    ipc1 = []
    llc_miss_rate1 = []
    l1d_miss_rate1 = []
    l1i_miss_rate1 = []
    l2_miss_rate1 = []
    file = "results{}.csv".format(i)
    g = open(file, "w")
    g.write("rep, ipc, llc_miss_rate, l1d_miss_rate, l1i_miss_rate, l2_miss_rate \n")
    for j in index:
        k = rep[j]
        f = open("results_30M/{}.trace.gz-bimodal-no-no-no-no-{}-1coreoption.txt".format(i,k),"r")
        lines = f.readlines()
        if j==4:
            a=lines[156].split()[4]
            ipc1.append(float(a))
            llc = lines[178].split()
            l1d = lines[157].split()
            l1i = lines[164].split()
            l2 = lines[171].split()
            b = float(llc[7])/float(llc[3])
            llc_miss_rate1.append(b)
            c = float(l1d[7])/float(l1d[3])
            l1d_miss_rate1.append(c)
            d = float(l1i[7])/float(l1i[3])
            l1i_miss_rate1.append(d)
            e = float(l2[7])/float(l2[3])
            l2_miss_rate1.append(e)
        else:
            a=lines[27].split()[4]
            ipc1.append(float(a))
            llc = lines[49].split()
            l1d = lines[28].split()
            l1i = lines[35].split()
            l2 = lines[42].split()
            b = float(llc[7])/float(llc[3])
            llc_miss_rate1.append(b)
            c = float(l1d[7])/float(l1d[3])
            l1d_miss_rate1.append(c)
            d = float(l1i[7])/float(l1i[3])
            l1i_miss_rate1.append(d)
            e = float(l2[7])/float(l2[3])
            l2_miss_rate1.append(e)
        g.write("{}, {}, {}, {}, {}, {} \n".format(k,str(a),str(b),str(c),str(d),str(e)))
    ipc.append(ipc1)
    llc_miss_rate.append(llc_miss_rate1)
    l1d_miss_rate.append(l1d_miss_rate1)
    l1i_miss_rate.append(l1i_miss_rate1)
    l2_miss_rate.append(l2_miss_rate1)
