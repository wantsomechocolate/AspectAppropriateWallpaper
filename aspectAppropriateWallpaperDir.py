##  Imports
from win32api import GetSystemMetrics
import ctypes, time, os, random, math
##http://nullege.com/codes/search/win32con.SPI_GETDESKWALLPAPER
import win32gui, win32con
from PIL import Image

##  Functions
def getdir():
    return "C:\Users\jmcglynn\Pictures\Desktop Backgrounds\DTBG"

def imgExtCheck(path):
    return True

def get_SAR():
    return float(GetSystemMetrics (0))/float(GetSystemMetrics (1))

def get_rand(list):
    return list[int(math.floor(random.random()*len(list)))]

def set_aspect_appropriate_img(SAR):
    if SAR>1:
        img_path=get_rand(landscapeList)
    elif SAR<1:
        img_path=get_rand(portraitList)
    ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, img_path , 0)

    return img_path

def get_IAR():
    current_image=win32gui.SystemParametersInfo(Action=win32con.SPI_GETDESKWALLPAPER)
    im = Image.open(current_image)
    return float(im.size[0])/float(im.size[1])

def compare_aspects(SAR,IAR):
    if IAR>=(1-tol)*SAR and IAR<=(1+tol)*SAR:
        return True
    else: return False

##  Constants
SPI_SETDESKWALLPAPER = 20
tol=0.2

##  Screen Data
screen_dim1=GetSystemMetrics (0)
screen_dim2=GetSystemMetrics (1)
screen_change=(screen_dim1+screen_dim2)/2
screen_aspect_ratio=float(screen_dim1)/float(screen_dim2)
print screen_aspect_ratio

##  Initializations
landscapeList=[]
portraitList=[]
directory=getdir()
dirContents=os.listdir(directory)

##  Separate images into landscape and portrait
for item in dirContents:
    item_path=directory+"\\"+item
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

##  Checking Functionality (Remove Later)
for item in landscapeList:
    print item[item.rindex("\\")+1:],
print ""
for item in portraitList:
    print item[item.rindex("\\")+1:],

##  The Actual Program
current_image = set_aspect_appropriate_img(get_SAR())
while True:
    SAR=get_SAR()
    IAR=get_IAR()
    print "Current Image: "+current_image
    if compare_aspects(get_SAR(),get_IAR()):
        print "SAR: "+str(SAR)
        print "IAR: "+str(IAR)
    else:
        print "made it!"
        current_image = set_aspect_appropriate_img(get_SAR())
    time.sleep(.1)

##---Delete below when program works to satisfaction - it is all older stuff---##

######lc=0
######pc=0
######lll=len(landscapeList)
######pll=len(portraitList)
######cli=landscapeList[lc]
######cpi=portraitList[pc]
####
#####print initialWidth, lll
####
######if initialWidth>screenChange:
######    currentOrientation="Landscape"
######    lc=int((random.random()*lll))
######    ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, landscapeList[lc] , 0)
######else:
######    currentOrientation="Portrait"
######    pc=int((random.random()*pll))
######    ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, portraitList[pc] , 0)
######
######print currentOrientation,lc,landscapeList[lc]
####
####
######true = 1
######initialWidth = GetSystemMetrics (0)
######if initialWidth < screenChange:
######    ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, portraitImage , 0)
######else:
######    ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, landscapeImage , 0)
######
######currentWidth = initialWidth
######while true==1:
######    time.sleep(.1)
######    currentWidth = GetSystemMetrics (0)
######    #print currentWidth
######    if currentWidth != initialWidth:
######        print "Resolution Changed"
######        if currentWidth > screenChange:
######            print "Current Width was greater than "+str(screenChange)
######            currentImage=landscapeImage
######            initialWidth = GetSystemMetrics (0)
######            ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, currentImage , 0)
######
######        elif currentWidth < screenChange:
######            print "Current Width was less than "+str(screenChange)
######            currentImage=portraitImage
######            initialWidth = GetSystemMetrics (0)
######            ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, currentImage , 0)
            

        

