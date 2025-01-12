import tkinter as tk
from tkinter import ttk
import data_handler  # Assume alert data is stored in the same database as packet data

class AlertHistoryView(tk.Frame):
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

        self.update_alert_history()

    def update_alert_history(self):
        # You'll need to implement logic to fetch alerts from the data_handler 
        # (potentially by filtering based on a 'alert' flag or column in the database)
        alerts = self.data_handler.retrieve_alerts()  # Replace with your alert retrieval logic
        for i, alert in enumerate(alerts):
            self.tree.insert("", "end", values=(alert[0], alert[1], alert[2], alert[3], alert[4], alert[5]))
