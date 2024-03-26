import csv

with open('builds.csv', 'r') as file:
    csvreader = csv.reader(file)
    cpus = []
    motherboards = []
    rams = []
    gpus = []
    psus = []
    for row in csvreader:
        cpus.append(row[2])
        motherboards.append(row[3])
        rams.append(row[4])
        gpus.append(row[5])
        psus.append(row[6])
cpus.pop(0)    
motherboards.pop(0)
rams.pop(0)
gpus.pop(0)
psus.pop(0)


cpuschanged=[]
def removeunwantedforCPU(cpus):
    for cpu in cpus:
        cpulist=cpu.split(" ")
        if cpulist[0] == "Intel":
            cpuchanges=cpulist[0]+" "+cpulist[1]+" "+cpulist[2]
            cpuschanged.append(cpuchanges)
        else:
            cpuchanges=cpulist[0]+" "+cpulist[1]+" "+cpulist[2]+" "+cpulist[3]
            cpuschanged.append(cpuchanges)
        
removeunwantedforCPU(cpus)


gpuschanged=[]
def removeunwantedforGPU(gpus):
    for gpu in gpus[0:10]:
        if "RTX 4060" in gpu:
            gpuschanged.append("RTX 4060")
        elif "RTX 4060 Ti" in gpu:
            gpuschanged.append("RTX 4060 Ti")
        elif "RTX 4070" in gpu:
            gpuschanged.append("RTX 4070")
        elif "RTX 4070 Ti" in gpu:
            gpuschanged.append("RTX 4070 Ti")
        elif "RTX 4080" in gpu:
            gpuschanged.append("RTX 4080")
        elif "RTX 4090" in gpu:
            gpuschanged.append("RTX 4090")
    print(gpuschanged)
        
removeunwantedforGPU(gpus)
        