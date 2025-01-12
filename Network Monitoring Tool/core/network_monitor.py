import scapy.all as scapy
import data_handler

class NetworkMonitor:
    def __init__(self, interface):
        self.interface = interface

    def start_monitoring(self):
        while True:
            # Capture packets
            packet = scapy.sniff(iface=self.interface, count=1)
            # Extract metadata
            metadata = {
                "timestamp": packet.time,
                "source_ip": packet[scapy.IP].src,
                "destination_ip": packet[scapy.IP].dst,
                "protocol": packet[scapy.IP].proto,
                "port": packet[scapy.TCP].dport if packet.haslayer(scapy.TCP) else packet[scapy.UDP].dport,
                "packet_size": len(packet),
            }
            # Store metadata in data_handler
            data_handler.store_metadata(metadata)