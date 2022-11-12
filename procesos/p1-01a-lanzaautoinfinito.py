import subprocess
try:
    subprocess.run("p1-01a-lanzaautoinfinito")
except subprocess.CalledProcessError as e:
    print(e.output)
   