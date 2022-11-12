import subprocess
try:
    #subprocess.run("Notepad.exe")
    #subprocess.run(["Notepad.exe"])
    #subprocess.run(["Notepad.exe",])
    #subprocess.run(["Notepad.exe","texto.txt"])
    #subprocess.run("C:/windows/system32/notepad.exe")
    #subprocess.run(["python","media.py"])
    #subprocess.run(["PowerShell","python media.py"])
    subprocess.run("calc.exe")
except subprocess.CalledProcessError as e:
    print(e.output)