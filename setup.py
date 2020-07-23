from setuptools import setup, find_packages
from sys import platform

if platform == "linux":
    setup(name="tkAudioConverter",
        author="Quin Brown",
        author_email="quinb96@protonmail.com",
        version="1.0",
        description="A gui audio converter that converts the most common audio formats.",
        install_requires=["pydub", "ttkthemes"],
        url="https://github.com/sketchyboi14/tkAudioConverter",
        platforms=["Linux"],
        include_package_data=True,
        zip_safe=False,
        packeges=find_packages(),
        )

elif platform == "win32":
    from cx_Freeze import setup, Executable
    from sys import platform

    build_exe_options = {"packages": ["pydub", "ttkthemes"]}
    setup(name="tkAudioConverter",
        version="1.0",
        author="Quin Brown",
        author_email="quinb96@protonmail.com",
        description="A gui audio converter that converts the most common audio formats.",
        install_requires=["pydub", "ttkthemes"],
        platforms=["Windows"],
        include_package_data=True,
        options = {"build_exe": build_exe_options},
        executables = [Executable("tkAudioConverter.py", icon="icons/appicon.ico", shortcutName="tkAudioConverter", shortcutDir="DesktopFolder",)])
