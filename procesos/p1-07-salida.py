from asyncio import subprocess
from sys import stderr, stdin, stdout

p1 = subprocess.Popen('dir', shell=True, stdin=None, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

while True:
    line = p1.stdout.readline()
    if not line:
        break
    print (line.rstrip())