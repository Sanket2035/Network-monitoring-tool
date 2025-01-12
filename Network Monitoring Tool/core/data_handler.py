import sqlite3

class DataHandler:
    def __init__(self, db_file="network_data.db"):
        self.conn = sqlite3.connect(db_file)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS packets (
                timestamp REAL,
                source_ip TEXT,
                destination_ip TEXT,
                protocol INTEGER,
                port INTEGER,
                packet_size INTEGER
            )
        """)
        self.conn.commit()

    def store_metadata(self, metadata):
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO packets VALUES (
                ?, ?, ?, ?, ?, ?
            )
        """, (
            metadata["timestamp"], metadata["source_ip"], metadata["destination_ip"], 
            metadata["protocol"], metadata["port"], metadata["packet_size"]
        ))
        self.conn.commit()

    def retrieve_metadata(self, filter_criteria=None):
        # Implement filtering logic based on criteria
        cursor = self.conn.cursor()
        if filter_criteria:
            # Apply filtering based on filter_criteria
            pass 
        else:
            cursor.execute("SELECT * FROM packets")
        rows = cursor.fetchall()
        return rows