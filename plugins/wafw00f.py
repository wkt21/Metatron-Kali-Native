import subprocess

class Plugin:
    name = "wafw00f"

    def run(self, target):
        cmd = ["wafw00f", target]
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout
