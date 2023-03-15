from os import system
import subprocess
import asyncio

async def showNotepad2():  
  try:
    await asyncio.create_subprocess_exec('notepad.exe')
  except subprocess.CalledProcessError as e:
      print(e.output)

async def autollamada():  
  try:
    await asyncio.create_subprocess_exec("python", "P1-09-infinito.py")
  except subprocess.CalledProcessError as e:
      print(e.output)

async def main():
  print ("inicio llamada asíncrona")
  await autollamada()
  await showNotepad2()
  print ("fin llamada asíncrona")
  print("pulsa una tecla para terminar")
  system ('Pause')
  
asyncio.run(main())