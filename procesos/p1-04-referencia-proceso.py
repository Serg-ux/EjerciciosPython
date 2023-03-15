import subprocess

def iniciarPrograma():
    try:
        SW_SHOWMAXIMIZED = 3
        info = subprocess.STARTUPINFO()
        info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        info.wShowWindow = SW_SHOWMAXIMIZED
        proc = subprocess.Popen('Notepad.exe', startupinfo=info)
        return proc
    except subprocess.CalledProcessError as e:
        print (e.output)
p = iniciarPrograma()
print ("El PId de este proceso es: ",str(p.pid))
input("Pulsa una tecla para terminar la ejecución")