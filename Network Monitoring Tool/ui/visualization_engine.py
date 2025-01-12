import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import data_handler

class VisualizationEngine(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(expand=True, fill="both")

        self.data_handler = data_handler.DataHandler()

        # Create Matplotlib Figure and Axes
        self.fig, self.ax = plt.subplots(figsize=(6, 4))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # ... (Add other visualizations as needed)

        self.update_visualization()

    def update_visualization(self):
        # Get data from data_handler
        metadata = self.data_handler.retrieve_metadata()

        # Example: Plot packet count over time
        timestamps = [packet[0] for packet in metadata]
        packet_counts = [i for i in range(len(metadata))]

        # Clear previous plot
        self.ax.clear()

        # Create the plot
        self.ax.plot(timestamps, packet_counts)
        self.ax.set_xlabel("Timestamp")
        self.ax.set_ylabel("Packet Count")

        # Update canvas
        self.canvas.draw()

        # Call update_visualization again after a delay
        self.after(1000, self)