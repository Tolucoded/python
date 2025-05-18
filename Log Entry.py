# Define the LogEntry class
class LogEntry:
    def __init__(self, timestamp, source_ip, dest_ip, event_type, message):
        self.timestamp = timestamp
        self.source_ip = source_ip
        self.dest_ip = dest_ip
        self.event_type = event_type
        self.message = message

    def is_alert(self):
        return self.event_type.lower() in ["alert", "critical", "malware"]

    def summarize(self):
        return f"[{self.timestamp}] {self.source_ip} ➜ {self.dest_ip} | {self.event_type.upper()}: {self.message}"

    def is_from_internal(self):
        return self.source_ip.startswith("192.168.") or self.source_ip.startswith("10.")

# Create a log entry object
log1 = LogEntry(
    "2025-05-18 12:45:00",
    "192.168.1.10",
    "8.8.8.8",
    "alert",
    "Suspicious outbound connection detected"
)
# Use its methods
print(log1.summarize())

# [2025-05-18 12:45:00] 192.168.1.10 ➜ 8.8.8.8 | ALERT: Suspicious outbound connection detected

print(log1.is_alert())
# True

print(log1.is_from_internal())
# True
