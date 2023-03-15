import subprocess
try:
    subprocess.run(["ping", "www.google.com","-n","5"])
except subprocess.CalledProcessError as e:
    print (e.output)
