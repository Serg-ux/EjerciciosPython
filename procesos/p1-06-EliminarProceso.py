import psutil

for proc in psutil.process_iter():
    try:
        nombreProceso = proc.name()
        if proc.name() == "Notepad.exe":
            PID = proc.pid
            print ("Eliminando el  porceso:", nombreProceso, " ::: ", PID)
            proc.kill()
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        print ("error")