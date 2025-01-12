import netifaces
import socket
import datetime
import platform

class SystemInfo:
    def __init__(self):
        self.interfaces = self.get_network_interfaces()
        self.connected_ip = self.get_connected_ip()
        self.date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.os_details = platform.platform()

    def get_network_interfaces(self):
        interfaces = []
        for interface in netifaces.interfaces():
            addresses = netifaces.ifaddresses(interface)
            if netifaces.AF_INET in addresses:
                interfaces.append((interface, addresses[netifaces.AF_INET]))
        return interfaces

    def get_connected_ip(self):
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        return ip