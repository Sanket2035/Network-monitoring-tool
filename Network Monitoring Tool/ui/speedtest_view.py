import tkinter as tk
from tkinter import ttk
import speedtest

class SpeedtestView(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(expand=True, fill="both")

        self.st = speedtest.Speedtest()

        self.download_label = ttk.Label(self, text="Download Speed:")
        self.download_label.pack()

        self.upload_label = ttk.Label(self, text="Upload Speed:")
        self.upload_label.pack()

        self.ping_label = ttk.Label(self, text="Ping:")
        self.ping_label.pack()

        self.run_speedtest_button = ttk.Button(self, text="Run Speed Test", command=self.run_test)
        self.run_speedtest_button.pack()

    def run_test(self):
        self.st.download()
        self.st.upload()
        self.st.get_best_server()

        self.download_label.config(text=f"Download Speed: {self.st.results.download} Mbps")
        self.upload_label.config(text=f"Upload Speed: {self.st.results.upload} Mbps")
        self.ping_label.config(text=f"Ping: {self.st.results.ping} ms")