from __future__ import unicode_literals
import youtube_dl
import tkinter as tk

class UI():
	def __init__(self):
		window=tk.Tk()
		window.geometry("350x150")
		window.title("Youtube to MP3 Downloader")
		url = tk.Label(text = "URL")
		url.grid(column=0,row=1)
		urlEntry = tk.Entry()
		urlEntry.grid(column=1,row=1)

		def getInput():
			url = urlEntry.get()
			code = self.download_and_transform(url)

			textArea = tk.Text(master=window,height=10,width=25)
			textArea.grid(column=1,row=6)
			answer = code
			textArea.insert(tk.END, answer)

		button=tk.Button(window,text="Start Download!", command=getInput, bg="green")
		button.grid(column=1,row=5)
		window.mainloop()

	def download_and_transform(self, url):
		ydl_opts = {
			'format': 'bestaudio/best',
			'postprocessors': [{
				'key': 'FFmpegExtractAudio',
				'preferredcodec': 'mp3',
				'preferredquality': '192',
			}],
		}

		with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		    return ydl.download([url])


UI()