#coding=utf-8
#setup.py、
#打包msi:python setup.py bdist_msi 
#打包exe:python setup.py build
import sys, os
from cx_Freeze import setup, Executable
 
__version__ = "1.1.2"
 
include_files = ['xio.ico','source']
excludes = ["tkinter"]
packages = ['random','time','sys','easygui']

base = None
if sys.platform == "win32":
    base = "Win32GUI"
setup(
name = "xio_FSE easygui edition",
description='made for wwc',
author='dgklpd',
version=__version__,
options = {"build_exe": {
'packages': packages,
'include_files': include_files,
'excludes': excludes,
'include_msvcr':True,
}},
executables = [Executable("xio.pyw",icon='xio.ico',base='win32gui')]
)
