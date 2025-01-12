import tkinter as tk
from tkinter import ttk
import network_monitor

class SettingsView(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(expand=True, fill="both")

        self.system_info = system_info.SystemInfo()

        # Network Interface Selection
        interface_label = ttk.Label(self, text="Network Interface:")
        interface_label.pack()

        self.interface_var = tk.StringVar(self)
        self.interface_var.set(self.system_info.interfaces[0][0])  # Default interface

        interface_dropdown = ttk.Combobox(self, textvariable=self.interface_var, values=[i[0] for i in self.system_info.interfaces])
        interface_dropdown.pack()

        # Save Button (update network monitor)
        save_button = ttk.Button(self, text="Save Settings", command=self.save_settings)
        save_button.pack()

    def save_settings(self):
        selected_interface = self.interface_var.get()
        # Update the network monitor with the new interface
        # ... (You might need to restart the network monitor or handle interface changes dynamically)