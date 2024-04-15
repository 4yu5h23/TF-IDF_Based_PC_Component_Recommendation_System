import csv
import re

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
        elif cpulist[0] == "AMD" and cpulist[1] == "Ryzen":
            cpuchanges=cpulist[0]+" "+cpulist[1]+" "+cpulist[2]+" "+cpulist[3]
            cpuschanged.append(cpuchanges)
        else:
            cpuschanged.append(cpu)
        
removeunwantedforCPU(cpus)


gpuschanged=[]
def removeunwantedforGPU(gpus):
    for gpu in gpus:
        if "RTX 4060 Ti" in gpu:
            gpuschanged.append("RTX 4060 Ti")
        elif "RTX 4060" in gpu:
            gpuschanged.append("RTX 4060")
        elif "RTX 4070 Ti" in gpu:
            gpuschanged.append("RTX 4070 Ti")
        elif "RTX 4070" in gpu:
            gpuschanged.append("RTX 4070")
        elif "RTX 4080" in gpu:
            gpuschanged.append("RTX 4080")
        elif "RTX 4090" in gpu:
            gpuschanged.append("RTX 4090")
        else:
            gpuschanged.append(gpu)
         
removeunwantedforGPU(gpus)

psuschanged=[]
def removeunwantedforPSU(psus):
    for psu in psus:
        psulist=psu.split(" ")
        for i in range(1,len(psulist)):
            if psulist[i]=="W":
                psuchanges=psulist[i-1]+" "+psulist[i]
                psuschanged.append(psuchanges)
                break

removeunwantedforPSU(psus)

ramchanged=[]
def removeunwantedforRAM(rams):
    for ram in rams:
        ramlist=ram.split(" ")
        for i in range(1,len(ramlist)):
            if  ramlist[i]=="GB":
                ramchanges=ramlist[i-1]+" "+ramlist[i]+" "+ramlist[i+1]+" "+ramlist[i+2]+" "+ramlist[i+3]+" "+ramlist[i+4]+" "+ramlist[i+5]
                ramchanged.append(ramchanges)
                break

removeunwantedforRAM(rams)


motherboardschanged=[]
def removeunwantedforMotherboard(motherboards):
    for motherboard in motherboards:
        match = re.search(r'\b(B[0-9]+\S*|Z[0-9]+\S*|X[0-9]+\S*)\b', motherboard)
        if match:
            motherboardschanged.append(match.group(0))
        else:
            motherboardschanged.append(motherboard)
removeunwantedforMotherboard(motherboards)
print(len(cpuschanged))
print(len(ramchanged))
print(len(motherboardschanged))
print(len(gpuschanged))
print(len(psuschanged))

with open('buildsfinal2.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Build No.','CPU','Motherboard','RAM','GPU','PSU'])
    for i in range(len(cpuschanged)):
        writer.writerow([i+1,cpuschanged[i],motherboardschanged[i],ramchanged[i],gpuschanged[i],psuschanged[i]])

        