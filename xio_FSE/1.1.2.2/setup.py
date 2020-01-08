import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os","sys","easygui","random","time","tkinter"],"include_files": ['xio.ico','source'], "excludes": ["tkinter"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "xio_FSE_easygui_edition",
        version = "1.1.2",
        description = "made for xio",
        options = {"build_exe": build_exe_options},
        executables = [Executable("xio.py",icon='xio.ico',shortcutName='xio人机大战前端版',shortcutDir='C:/Users/Administrator/Desktop', base=base)])
