from cx_Freeze import setup, Executable


build_exe_options = {"packages": ["pydub", "os", "webbrowser", "ttkthemes"]}


setup(name = "tkAudioConverter",
      version = "1.0",
      description = "An audio converter written in python3 using the tkinter module",
      options = {"build_exe": build_exe_options},
      executables = [Executable("tkAudioConverter.py", icon="appicon.ico", shortcutName="tkAudioConverter", shortcutDir="DesktopFolder",)])
