#instalar psutil: pip install psutil
import psutil

try:
    for proc in psutil.process_iter():
        #obrenr el nombre y el PID de cada proceso
        processName = proc.name()
        processID = proc.pid
        print (processName, " ::: ", processID)

#except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
except:
    print ("error")