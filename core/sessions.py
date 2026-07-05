import uuid
import time

class Session:
    def __init__(self, target):
        self.id = str(uuid.uuid4())
        self.target = target
        self.timestamp = time.time()
        self.recon = {}
        self.analysis = {}

    def add_recon(self, tool_name, data):
        self.recon[tool_name] = data

    def add_analysis(self, data):
        self.analysis = data

    def to_dict(self):
        return {
            "id": self.id,
            "target": self.target,
            "timestamp": self.timestamp,
            "recon": self.recon,
            "analysis": self.analysis
        }
