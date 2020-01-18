#coding=utf-8
#setup.py
#打包msi:python setup.py bdist_msi 
#打包exe:python setup.py build
import sys, os
from cx_Freeze import setup, Executable
 
__version__ = "1.1.3"
 
include_files = []
excludes = ["tkinter"]
packages = ['random','time']
 
setup(
name = "xio_SCE console edition",
description='made for wwc',
author='dgklpd',
version=__version__,
options = {"build_exe": {
'packages': packages,
'include_files': include_files,
'excludes': excludes,
'include_msvcr':True,
}},
executables = [Executable("xio.py",icon='xio.ico')]
)
