from distutils.log import info
from re import sub
import subprocess
def iniciar_programa():
    try:
        SW_SHOWMAXIMIZED=3
        info= subprocess.STARTUPINFO()
        info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        info.wShowWindow=SW_SHOWMAXIMIZED
        subprocess.Popen("Notepad.exe",startupinfo=info)
    except subprocess.CalledProcessError as e:
        print(e.output)
iniciar_programa()
input("pulsa una tecla para terminar la ejecución")