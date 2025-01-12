import tkinter as tk
from tkinter import ttk
import core.network_monitor
import core.analysis_engine
import core.data_handler
import core.reporting
import core.system_info
import log_view
import speedtest_view
import settings_view
import alert_history_view
import visualization_engine

class NetworkAnalyzer(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Network Analyzer")

        self.system_info = system_info.SystemInfo()

        # ... (UI initialization and tab creation)

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill="both")

        self.log_tab = log_view.LogView(self.notebook)
        self.speedtest_tab = speedtest_view.SpeedtestView(self.notebook)
        self.settings_tab = settings_view.SettingsView(self.notebook)
        self.alert_history_tab = alert_history_view.AlertHistoryView(self.notebook)
        self.visualization_tab = visualization_engine.VisualizationEngine(self.notebook)

        self.notebook.add(self.log_tab, text="Log")
        self.notebook.add(self.speedtest_tab, text="Speed Test")
        self.notebook.add(self.settings_tab, text="Settings")
        self.notebook.add(self.alert_history_tab, text="Alert History")
        self.notebook.add(self.visualization_tab, text="Visualization")

        self.network_monitor = network_monitor.NetworkMonitor(self.system_info.interfaces[0][0])
        self.analysis_engine = analysis_engine.AnalysisEngine()
        self.data_handler = data_handler.DataHandler()

        # Start the network monitor
        self.network_monitor.start_monitoring()

        # Periodically run the analysis engine
        self.after(1000, self.update_analysis)  # Run every 1 second

    def update_analysis(self):
        self.analysis_engine.analyze()
        self.after(1000, self.update_analysis) 

# Create the main application
app = NetworkAnalyzer()
app.mainloop()