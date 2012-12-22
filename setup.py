from distutils.core import setup
import py2exe

setup(windows=['aawp.py'])

## Download and install py2exe
## Navigate to the directory with the setup file and aawp.py
## Type python setup.py py2exe
## And put a shorcut to the exe in
## C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup
## Or wherever your startup folder is. 
