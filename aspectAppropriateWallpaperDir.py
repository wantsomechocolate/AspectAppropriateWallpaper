from win32api import GetSystemMetrics
import ctypes
import time
import os
import random, math

##import ctypes
##user32 = ctypes.windll.user32
##screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

SPI_SETDESKWALLPAPER = 20
##landscapeImage="C:\Users\jmcglynn\Pictures\Desktop Backgrounds\DTBG\Landscape\Landscape.jpg"
##portraitImage="C:\Users\jmcglynn\Pictures\Desktop Backgrounds\DTBG\Portrait\Portrait.jpg"

landscapeDir="C:\Users\jmcglynn\Pictures\Desktop Backgrounds\DTBG\Landscape"
portraitDir="C:\Users\jmcglynn\Pictures\Desktop Backgrounds\DTBG\Portrait"

landscapeDirContents=os.listdir(landscapeDir)
portraitDirContents=os.listdir(portraitDir)

landscapeList=[]
portraitList=[]

for item in landscapeDirContents:
    if os.path.isfile(landscapeDir+"\\"+item):
        landscapeList.append(landscapeDir+"\\"+item)
    else:pass

for item in portraitDirContents:
    if os.path.isfile(portraitDir+"\\"+item):
        portraitList.append(portraitDir+"\\"+item)
    else:pass


##print landscapeList
##print portraitList

lc=0
pc=0
lll=len(landscapeList)
pll=len(portraitList)
cli=landscapeList[lc]
cpi=portraitList[pc]


initialWidth=GetSystemMetrics (0)
otherWidth=GetSystemMetrics (1)
screenChange=(initialWidth+otherWidth)/2

#print initialWidth, lll

if initialWidth>screenChange:
    currentOrientation="Landscape"
    lc=int((random.random()*lll))
    ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, landscapeList[lc] , 0)
else:
    currentOrientation="Portrait"
    pc=int((random.random()*pll))
    ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, portraitList[pc] , 0)

print currentOrientation,lc,landscapeList[lc]


##true = 1
##initialWidth = GetSystemMetrics (0)
##if initialWidth < screenChange:
##    ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, portraitImage , 0)
##else:
##    ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, landscapeImage , 0)
##
##currentWidth = initialWidth
##while true==1:
##    time.sleep(.1)
##    currentWidth = GetSystemMetrics (0)
##    #print currentWidth
##    if currentWidth != initialWidth:
##        print "Resolution Changed"
##        if currentWidth > screenChange:
##            print "Current Width was greater than "+str(screenChange)
##            currentImage=landscapeImage
##            initialWidth = GetSystemMetrics (0)
##            ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, currentImage , 0)
##
##        elif currentWidth < screenChange:
##            print "Current Width was less than "+str(screenChange)
##            currentImage=portraitImage
##            initialWidth = GetSystemMetrics (0)
##            ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, currentImage , 0)
            

        

