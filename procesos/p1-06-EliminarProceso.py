import psutil

for proc in psutil.process_iter():
    try:
        nombreProceso = proc.name()
        if proc.name() == "notepad.exe":
            PID = proc.pid
            print ("Eliminando el  porceso:", nombreProceso, " ::: ", PID)
            proc.kill()
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        print ("error")
        


for proc in psutil.process_iter():
    try:
        nombreProceso = proc.name()
        if proc.name() == "chrome.exe":
            PID = proc.pid
            print("Eliminando el proceso:", nombreProceso, " ::: ", PID)
            proc.kill()
    except(psutil.psutil.NoSuchProcess, psutil.psutil.AccessDenied, psutil.psutil.ZombieProcess):
        print("error")