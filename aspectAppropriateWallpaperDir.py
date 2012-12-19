from win32api import GetSystemMetrics
import ctypes
import time
import os
import random, math
from PIL import Image

SPI_SETDESKWALLPAPER = 20

##landscapeDir="C:\Users\jmcglynn\Pictures\Desktop Backgrounds\DTBG\Landscape"
##portraitDir="C:\Users\jmcglynn\Pictures\Desktop Backgrounds\DTBG\Portrait"

def getdir():
    return "C:\Users\jmcglynn\Pictures\Desktop Backgrounds\DTBG"
directory=getdir()

def imgExtCheck(path):
    return True

##landscapeDirContents=os.listdir(landscapeDir)
##portraitDirContents=os.listdir(portraitDir)
dirContents=os.listdir(directory)

landscapeList=[]
portraitList=[]
tol=0.15

screen_dim1=GetSystemMetrics (0)
screen_dim2=GetSystemMetrics (1)
screen_change=(screen_dim1+screen_dim2)/2

for item in dirContents:
    item_path=directory+"\\"+item
    if os.path.isfile(item_path):
        if imgExtCheck(item_path):
            im = Image.open(item_path)
            asRat = float(im.size[0])/float(im.size[1])
            if asRat>=(1-tol)*
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
            

        

