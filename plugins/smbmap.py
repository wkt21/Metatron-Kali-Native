import subprocess

class Plugin:
    name = "smbmap"

    def run(self, target):
        cmd = ["smbmap", "-H", target]
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout
