import subprocess
try:
    # subprocess.run("Notepad.exe")
    # subprocess.run(["Notepad.exe",])
    # subprocess.run(["Notepad.exe"])
    # subprocess.run("C:/windows/system32/notepad.exe")
    # subprocess.run(['Notepad.exe','texto.txt'])
    # subprocess.run(["python","media.py"])
    #subprocess.run(["PowerShell","python media.py"])
    print ("hola")
    subprocess.run(["python", "P1-01a-LanzaAutoInfinito.py"])
except subprocess.CalledProcessError as e:
    print (e.output)
