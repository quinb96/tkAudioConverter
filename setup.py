from setuptools import setup, find_packages

setup(name="tkAudioConverter",
      author="Quin Brown",
      author_email="quinb96@protonmail.com",
      version="1.0",
      description="A gui audio converter that converts the most common audio formats.",
      install_requires=["pydub", "ttkthemes"],
      url="https://github.com/sketchyboi14/tkAudioConverter",
      platforms=["Linux", "Windows"],
      include_package_data=True,
      zip_safe=False,
      packeges=find_packages(),
      )
