import tkinter as tk
from tkinter import ttk
import data_handler

class LogView(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(expand=True, fill="both")

        self.data_handler = data_handler.DataHandler()
        self.tree = ttk.Treeview(self, columns=("timestamp", "source_ip", "destination_ip", "protocol", "port", "packet_size"), show="headings")
        self.tree.heading("timestamp", text="Timestamp")
        self.tree.heading("source_ip", text="Source IP")
        self.tree.heading("destination_ip", text="Destination IP")
        self.tree.heading("protocol", text="Protocol")
        self.tree.heading("port", text="Port")
        self.tree.heading("packet_size", text="Packet Size")
        self.tree.pack(expand=True, fill="both")

        self.update_log()

    def update_log(self):
        metadata = self.data_handler.retrieve_metadata()
        for i, packet in enumerate(metadata):
            self.tree.insert("", "end", values=(packet[0], packet[1], packet[2], packet[3], packet[4], packet[5]))
        self