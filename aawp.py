## Change your own settings from the control panel (tile,fit,etc)
## I just discovered a bug that happens when you let the program start
## running while in portraint mode. It starts cylcing through all
## AA wallpapers. When changed back to landscape it stops cycling,
## but if changed back to portrait it continues the behavior.
## When started in landscape mode, everything is fine. 

## Change line 15 to the directory of your images. 
## Have a nice day. 

##  Imports
from win32api import GetSystemMetrics
import ctypes, time, os, random, math
##http://nullege.com/codes/search/win32con.SPI_GETDESKWALLPAPER
import win32gui, win32con
from PIL import Image

##  Functions
def getdir():
    ## Put your own path here. 
    return "C:\Users\James McGlynn\Pictures\Desktop Pictures\AAWP"

def imgExtCheck(path):
    extensions=('png','jpg','jpeg','bmp','tiff')
    try:
        path_ext=path[path.rindex('.')+1:]
    except:
        path_ext="none"
    for item in extensions:
        if item == path_ext:
            return True
        else: pass
    return False

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

##  Initializations
landscapeList=[]
portraitList=[]
directory=getdir()
dirContents=os.listdir(directory)

##  Separate images into landscape and portrait
for item in dirContents:
    item_path=directory+"\\"+item
    if os.path.isfile(item_path):
        if imgExtCheck(item_path):
            im = Image.open(item_path)
            asRat = float(im.size[0])/float(im.size[1])
            if asRat>=(1-tol)*screen_aspect_ratio and asRat<=(1+tol)*screen_aspect_ratio:
                landscapeList.append(directory+"\\"+item)
            elif asRat>=(1-tol)*(1/screen_aspect_ratio) and asRat<=(1+tol)*(1/screen_aspect_ratio):
                portraitList.append(directory+"\\"+item)

######  Checking Functionality (Remove Later)
####for item in landscapeList:
####    print item[item.rindex("\\")+1:],
####print ""
####for item in portraitList:
####    print item[item.rindex("\\")+1:],

##  The Actual Program
current_image = set_aspect_appropriate_img(get_SAR())
while True:
    SAR=get_SAR()
    IAR=get_IAR()
    if compare_aspects(get_SAR(),get_IAR()):
        pass
    else:
        current_image = set_aspect_appropriate_img(get_SAR())
    time.sleep(.1)

