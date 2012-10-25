from win32api import GetSystemMetrics
import ctypes
import time

SPI_SETDESKWALLPAPER = 20
landscapeImage="C:\Users\James McGlynn\Pictures\Desktop Pictures\VB Project\Landscape.jpg"
portraitImage="C:\Users\James McGlynn\Pictures\Desktop Pictures\VB Project\Portrait.jpg"

currentImage=landscapeImage
currentOrientation="Landscape"
screenChange=1000

true = 1
initialWidth = GetSystemMetrics (0)
if initialWidth < screenChange:
    ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, portraitImage , 0)
else:
    ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, landscapeImage , 0)
#currentWidth = initialWidth
while true==1:
    time.sleep(.1)
    currentWidth = GetSystemMetrics (0)
    #print currentWidth
    if currentWidth != initialWidth:
        #print "Resolution Changed"
        if currentWidth > screenChange:
            #print "Current Width was greater than 1000"
            currentImage=landscapeImage
            initialWidth = GetSystemMetrics (0)
            ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, currentImage , 0)

        elif currentWidth < screenChange:
            #print "Current Width was less than 1000"
            currentImage=portraitImage
            initialWidth = GetSystemMetrics (0)
            ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, currentImage , 0)
            

        

