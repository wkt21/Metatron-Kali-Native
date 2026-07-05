import subprocess

class Plugin:
    name = "nikto"

    def run(self, target):
        cmd = ["nikto", "-h", target]
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout
