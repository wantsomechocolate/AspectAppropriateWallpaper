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
screen_aspect_ratio=float(screen_dim1)/float(screen_dim2)

print screen_aspect_ratio

for item in dirContents:
    item_path=directory+"\\"+item
    #print item_path
    print item
    if os.path.isfile(item_path):
        if imgExtCheck(item_path):
            im = Image.open(item_path)
            asRat = float(im.size[0])/float(im.size[1])
            print asRat
            print 1/asRat
            if asRat>=(1-tol)*screen_aspect_ratio and asRat<=(1+tol)*screen_aspect_ratio:
                landscapeList.append(directory+"\\"+item)
            elif asRat>=(1-tol)*(1/screen_aspect_ratio) and asRat<=(1+tol)*(1/screen_aspect_ratio):
                portraitList.append(directory+"\\"+item)

##Holy D!##$ It Works!   
print landscapeList
print portraitList

##So now I can continue as before with two separate lists one containing the "landscape images"
##and one containing the portrait ones. 


##lc=0
##pc=0
##lll=len(landscapeList)
##pll=len(portraitList)
##cli=landscapeList[lc]
##cpi=portraitList[pc]

#print initialWidth, lll

##if initialWidth>screenChange:
##    currentOrientation="Landscape"
##    lc=int((random.random()*lll))
##    ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, landscapeList[lc] , 0)
##else:
##    currentOrientation="Portrait"
##    pc=int((random.random()*pll))
##    ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, portraitList[pc] , 0)
##
##print currentOrientation,lc,landscapeList[lc]


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
            

        

