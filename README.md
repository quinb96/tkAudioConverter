For Linux and Windows

Install to Windows``https://github.com/sketchyboi14/tkAudioConverter/releases/tag/tkAC``

You need ffmpeg in order for this software to work.
However ffmpeg can't be downloaded anymore since the website hosting it was closed.
So I included ffmpeg in this repo.
To properly install ffmpeg follow these instructions.

Copy the ffmpeg folder, then paste it to C:\Program Files\

Next, go to your Windows search bar which is on the bottom left corner a white rectangle box.

Type "environment variables", without the quotes, then press "enter".

A System Properties window comes up. At the bottom right corner of the window, click "Environment Variables"

Another window pops up. There was two boxes. One that is "User variables for username"
and one that is "System Variables".

Under "System Variables" in the Variable column, click "Path", then click "Edit"

Another window appears. On the top right corner click "New".

Then type "C:\Program Files\ffmpeg\bin", then click "OK"

You're done. Windows should be able to find ffmpeg now.

Run as python script
```
git clone https://github.com/sketchyboi14/tkAudioConverter.git
cd tkAudioConverter
python3 tkAudioConverter.py
```




