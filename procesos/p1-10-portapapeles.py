import win32clipboard

#enviar al portapeles
win32clipboard.OpenClipboard()
win32clipboard.EmptyClipboard()
win32clipboard.SetClipboardText("Trucos A Carballeira By Carla")
win32clipboard.CloseClipboard()

#obtener datos del portapapeles
win32clipboard.OpenClipboard()
datos = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()
print (datos)
