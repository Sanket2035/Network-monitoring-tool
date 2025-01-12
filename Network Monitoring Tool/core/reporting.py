# core/reporting.py
import email_utils  # You'll need to implement email_utils.py 

class Reporting:
    def send_alert(self, packet):
        subject = "Network Anomaly Detected"
        body = f"""
        A potential network anomaly has been detected.
        
        Timestamp: {packet["timestamp"]}
        Source IP: {packet["source_ip"]}
        Destination IP: {packet["destination_ip"]}
        Protocol: {packet["protocol"]}
        Port: {packet["port"]}
        Packet Size: {packet["packet_size"]}
        """
        email_utils.send_email(subject, body)  # Use your email_utils module to send email