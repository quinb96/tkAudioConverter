import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from ttkthemes import themed_tk as tk
from tkinter import font
from pydub import AudioSegment
import os
import webbrowser

def closeapp(*args):
	root.destroy()

def open_github():
	webbrowser.open_new("https://github.com/sketchyboi14")

def aboutaudioconverter(*args):
	top = Toplevel()
	label = Label(top, text="tkAudioConverter was created by sketchyboi14 in Python. \nConvert any audio to mp3, flac, wav, or ogg. \nClick on the gihtub icon to visit my github page.", font=("Michroma", 10, "bold"))
	label.pack()

	githubiconbtn = Button(top, image=githubicon, command=open_github, relief="flat", cursor="plus")
	githubiconbtn.pack()

def curconvertto_flac():
	global sound
	global root3
	n = listbox.curselection()
	filesave = filedialog.asksaveasfilename(title="Save As Flac", defaultextension=".flac")
	sound.export(filesave, format="Flac")
	root3.destroy()
	if sound.export(filesave, format="Flac"):
		messagebox.showinfo("Successful", "Your audio file has been successfully converted to flac")

def curconvertto_ogg():
	global sound
	global root3
	n = listbox.curselection()
	filesave = filedialog.asksaveasfilename(title="Save As Ogg", defaultextension=".ogg")
	sound.export(filesave, format="ogg")
	root3.destroy()
	if sound.export(filesave, format="ogg"):
		messagebox.showinfo("Successful", "Your audio file has been successfully converted to ogg")

def curconvertto_mp3():
	global sound
	global root3
	n = listbox.curselection()
	filesave = filedialog.asksaveasfilename(title="Save As Mp3", defaultextension=".mp3")
	sound.export(filesave, format="mp3")
	root3.destroy()
	if sound.export(filesave, format="mp3"):
		messagebox.showinfo("Successful", "Your audio file has been successfully converted to mp3")

def curconvertto_wav():
	global sound
	global root2
	global n
	n = listbox.curselection()
	filesave = filedialog.asksaveasfilename(title="Save As Wav", defaultextension=".wav")
	sound.export(filesave, format="wav")
	root3.destroy()
	if sound.export(filesave, format="wav"):
		messagebox.showinfo("Successful", "Your audio file has been successfully converted to wav")

def currentselection(*args):
	global sound
	global root3
	root3 = tk.ThemedTk()
	root3.title("Select Format")
	root3.geometry("595x242")
	root3.get_themes()
	root3.set_theme("breeze")

	n = listbox.curselection()
	askquest = ttk.Label(root3, text="Select a format to convert to", font=("Michroma", 10, "bold"))
	mp3btn = ttk.Button(root3, text="Mp3", command=curconvertto_mp3)
	wavbtn = ttk.Button(root3, text="Wav", command=curconvertto_wav)
	oggbtn = ttk.Button(root3, text="Ogg", command=curconvertto_ogg)
	flacbtn = ttk.Button(root3, text="Flac", command=curconvertto_flac)

	askquest.pack(pady=10)
	mp3btn.pack(ipady=10, fill=X)
	wavbtn.pack(ipady=10, fill=X)
	oggbtn.pack(ipady=10, fill=X)
	flacbtn.pack(ipady=10, fill=X)

def convertto_flac():
	global sound
	global root2
	filesave = filedialog.asksaveasfilename(title="Save As Flac", defaultextension=".Flac")
	sound.export(filesave, format="Flac")
	root2.destroy()
	if sound.export(filesave, format="Flac"):
		messagebox.showinfo("Successful", "Your audio file has been successfully converted to wav")

def convertto_wav():
	global sound
	global root2
	filesave = filedialog.asksaveasfilename(title="Save As Wav", defaultextension=".wav")
	sound.export(filesave, format="wav")
	root2.destroy()
	if sound.export(filesave, format="wav"):
		messagebox.showinfo("Successful", "Your audio file has been successfully converted to wav")

def convertto_ogg():
	global sound
	global root2
	filesave = filedialog.asksaveasfilename(title="Save As Ogg", defaultextension=".ogg")
	sound.export(filesave, format="ogg")
	root2.destroy()
	if sound.export(filesave, format="ogg"):
		messagebox.showinfo("Successful", "Your audio file has been successfully converted to ogg")

def convertto_mp3():
	global sound
	global root2
	filesave = filedialog.asksaveasfilename(title="Save As Mp3", defaultextension=".mp3")
	sound.export(filesave, format="mp3")
	root2.destroy()
	if sound.export(filesave, format="wav"):
		messagebox.showinfo("Successful", "Your audio file has been successfully converted to mp3")

def convert_selection():
	global sound
	global root2
	root2 = tk.ThemedTk()
	root2.title("Select Format")
	root2.geometry("595x242")
	root2.get_themes()
	root2.set_theme("breeze")
	askquest = ttk.Label(root2, text="Select a format to convert to", font=("Michroma", 10, "bold"))
	mp3btn = ttk.Button(root2, text="Mp3", command=convertto_mp3)
	wavbtn = ttk.Button(root2, text="Wav", command=convertto_wav)
	oggbtn = ttk.Button(root2, text="Ogg", command=convertto_ogg)
	flacbtn = ttk.Button(root2, text="Flac", command=convertto_flac)

	askquest.pack(pady=10)
	mp3btn.pack(ipady=10, fill=X)
	wavbtn.pack(ipady=10, fill=X)
	oggbtn.pack(ipady=10, fill=X)
	flacbtn.pack(ipady=10, fill=X)

def open_file(*args):
	global sound
	file = filedialog.askopenfilename(initialdir="/home/quin/Music", title="Select Audio File", filetypes=(("Mp3 Files", "*.mp3"), ("All Files", "*.*")))
	audfile = open(file, "rb")
	sound = AudioSegment.from_file(audfile)
	listbox.insert(0, os.path.basename(file))
	convert_selection()

def add_to_entry(*args):
	n = listbox.curselection()
	item = listbox.get(n)
	v.set(item)

root = tk.ThemedTk()
root.get_themes()
root.set_theme("breeze")
root.geometry("350x210")
root.title("tkAudioConverter")
appicon = PhotoImage(file="icons/appicon.png")
root.iconphoto(False, appicon)

openicon = PhotoImage(file="icons/openicon.png")
githubicon = PhotoImage(file="icons/githubicon.png")
infoicon = PhotoImage(file="icons/infoicon.png")
closeicon = PhotoImage(file="icons/closeicon.png")

sound = ""
v = StringVar()

menu = Menu(root)
submenu = Menu(menu, tearoff=False)

menu.add_cascade(label="File", menu=submenu, font=("Meera", 10, "bold"))
submenu.add_command(label="Open File", compound=LEFT, font=("Meera", 10, "bold"), command=open_file, image=openicon, accelerator="Ctrl O")
submenu.add_command(label="Close", compound=LEFT, font=("Meera", 10, "bold"), command=root.destroy, image=closeicon, accelerator="Ctrl W")

submenu = Menu(menu, tearoff=False)
menu.add_cascade(label="Help", menu=submenu, font=("Meera", 10, "bold"))
submenu.add_command(label="About tkAudioConverter", font=("Meera", 10, "bold"), command=aboutaudioconverter, image=infoicon, compound=LEFT, accelerator="Ctrl H")

listbox = Listbox(root, width=50, height=10, bg="white")
listbox.pack()
listbox.bind("<ButtonRelease-1>", add_to_entry)
listbox.bind("<Double-Button>", currentselection)
root.bind("<Control-o>", open_file)
root.bind("<Control-w>", closeapp)
root.bind("<Control-h>", aboutaudioconverter)

label = ttk.Label(root, textvariable=v, font=("Michroma", 8, "bold"))
label.pack()

root.config(menu=menu)

root.mainloop()
