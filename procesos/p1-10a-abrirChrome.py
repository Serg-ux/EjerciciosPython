import subprocess
try:
   subprocess.run(["C:\Program Files\Google\Chrome\Application\chrome.exe", "www.google.com/search?q=libros_python"])
   
except subprocess.CalledProcessError as e:
    print (e.output)